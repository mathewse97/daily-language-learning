#!/usr/bin/env python3
"""Confere as invariantes que um arquivo pode conferir sozinho.

Roda em todo commit, pelo GitHub Actions, e localmente com:  python3 validate.py

O que ele NÃO confere está dito no fim deste arquivo, de propósito: um
validador que finge cobrir o que não cobre é pior que nenhum.
"""
import datetime as dt
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent
erros: list[str] = []
avisos: list[str] = []


def erro(msg: str) -> None:
    erros.append(msg)


def aviso(msg: str) -> None:
    avisos.append(msg)


# ---------------------------------------------------------------- léxico
def ler_lexico() -> dict[str, int]:
    """Devolve {termo: exp} das seções gregas."""
    p = ROOT / "state" / "lexicon.md"
    if not p.exists():
        erro("state/lexicon.md não existe")
        return {}
    texto = p.read_text(encoding="utf-8")
    bloco = re.search(r"```\n(.*?)```", texto, re.S)
    if not bloco:
        erro("state/lexicon.md não tem bloco de dados cercado por ```")
        return {}
    itens: dict[str, int] = {}
    formas: list[tuple[str, str, int]] = []
    secao = ""
    for linha in bloco.group(1).splitlines():
        linha = linha.strip()
        if not linha or linha.startswith(("FORMAT:", "STATUS:", "BOXES:", "RULE:",
                                          "EXPOS:", " ", "(")):
            continue
        if linha.startswith("["):
            secao = linha.split("]")[0] + "]"
            continue
        if "|" not in linha:
            continue
        campos = [c.strip() for c in linha.split("|")]
        if secao == "[GR-FORMA]":
            if len(campos) != 3:
                erro(f"léxico · [GR-FORMA] · linha com {len(campos)} campos, "
                     f"esperados 3 (forma | lema | exp): {linha}")
                continue
            try:
                formas.append((campos[0], campos[1], int(campos[2])))
            except ValueError:
                erro(f"léxico · exp não é número: {linha}")
        elif secao.startswith("[GR"):
            if len(campos) != 7:
                erro(f"léxico · {secao} · linha com {len(campos)} campos, "
                     f"esperados 7: {linha}")
                continue
            try:
                itens[campos[0]] = int(campos[6])
            except ValueError:
                erro(f"léxico · exp não é número: {linha}")
        elif secao in ("[IT-FALSI]", "[IT-INTERF]"):
            if len(campos) != 6:
                erro(f"léxico · {secao} · linha com {len(campos)} campos, "
                     f"esperados 6: {linha}")
        elif secao == "[EN-COLLOC]":
            if len(campos) != 3:
                erro(f"léxico · {secao} · linha com {len(campos)} campos, "
                     f"esperados 3: {linha}")
    # Forma sem lema não tem como herdar nada; e a soma das formas de um lema
    # não pode passar do exp dele, que conta todas as aparições.
    soma: dict[str, int] = {}
    for forma, lema, n in formas:
        if lema not in itens:
            erro(f"léxico · [GR-FORMA] · {forma!r} aponta para o lema {lema!r}, "
                 f"que não está no léxico")
            continue
        soma[lema] = soma.get(lema, 0) + n
    for lema, n in soma.items():
        if n > itens[lema]:
            erro(f"léxico · as formas de {lema!r} somam exp {n}, acima do exp do "
                 f"lema ({itens[lema]}) — o lema conta todas as aparições")
    return itens


# ---------------------------------------------------------------- pacote
def validar_semana(exp: dict[str, int]) -> None:
    p = ROOT / "state" / "week.json"
    if not p.exists():
        erro("state/week.json não existe")
        return
    try:
        d = json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        erro(f"week.json não é JSON válido — {e}")
        return

    if d.get("schema") != "acharnae-week/1":
        erro(f"week.json · schema é {d.get('schema')!r}, esperado 'acharnae-week/1'")

    frases = d.get("greek", {}).get("sentences", [])
    if not d.get("greek", {}).get("register"):
        erro("week.json · greek.register vazio — invariante 10 exige "
             "[composto], [adaptado] ou [autêntico]")

    for i, frase in enumerate(frases, 1):
        for j, palavra in enumerate(frase, 1):
            if not isinstance(palavra, list) or len(palavra) != 3:
                erro(f"week.json · frase {i}, palavra {j}: esperado "
                     f"[glosa, grego, transliteração]")
                continue
            glosa, grego, tr = palavra
            if not grego:
                erro(f"week.json · frase {i}, palavra {j}: grego vazio")
            if (glosa is None) != (tr is None):
                erro(f"week.json · frase {i}, palavra {j} ({grego}): glosa e "
                     f"transliteração têm de sumir juntas — invariante 17")

    dias = d.get("days", [])
    if len(dias) != 7:
        erro(f"week.json · {len(dias)} dias, esperados 7")
    esperados = [1, 2, 3, 4, 5, 6, 0]
    if [x.get("d") for x in dias] != esperados:
        erro(f"week.json · a ordem dos dias deve ser {esperados}")

    anterior = 0
    for dia in dias:
        rotulo = dia.get("label", dia.get("d"))
        cartoes = dia.get("cards", [])
        gregos = [c for c in cartoes if c.get("lang") == "gr"]
        if len(gregos) != 1:
            erro(f"week.json · {rotulo}: {len(gregos)} cartões de grego, esperado 1")
            continue
        c = gregos[0]

        up = c.get("upTo")
        if not isinstance(up, int):
            erro(f"week.json · {rotulo}: upTo ausente ou não inteiro")
            continue
        if up > len(frases):
            erro(f"week.json · {rotulo}: upTo {up} maior que o número de "
                 f"frases ({len(frases)})")
        if up < anterior:
            erro(f"week.json · {rotulo}: upTo {up} menor que o do dia anterior "
                 f"({anterior}) — invariante 12, o texto nunca encolhe")
        anterior = up

        if not c.get("sound"):
            erro(f"week.json · {rotulo}: falta a nota de som — invariante 14")
        if not c.get("pt"):
            erro(f"week.json · {rotulo}: falta o português corrido — invariante 14")

        forma = c.get("form")
        if forma is not None and (not isinstance(forma, str) or "\n" in forma
                                  or len(re.sub(r"<[^>]+>", "", forma)) > 360):
            erro(f"week.json · {rotulo}: a nota de forma é curta, até três linhas "
                 f"— invariante 14")
        for cc in cartoes:
            curio = cc.get("curio")
            if curio is not None and not re.search(r"\)\.?$", str(curio).strip()):
                erro(f"week.json · {rotulo}: a curiosidade ({cc.get('lang')}) tem de "
                     f"terminar com a fonte entre parênteses — invariante 23")
        # Números no italiano: algarismo sem o extenso logo depois, entre
        # parênteses, ele não sabe ler (invariante 19). O português da curiosidade
        # e da nota fica de fora: ali o número é lido em português.
        for cc in cartoes:
            if cc.get("lang") != "it":
                continue
            textos = [cc.get("text"), cc.get("setting"), cc.get("produce")]
            textos += cc.get("questions") or []
            textos += [p[1] for p in cc.get("answers") or []]
            textos += (cc.get("recall") or {}).get("prompts", [])
            textos += (cc.get("recall") or {}).get("key", [])
            for s in textos:
                for m in re.finditer(r"\d+(?!\d)(?! \()", str(s or "")):
                    erro(f"week.json · {rotulo}: o número {m.group()} no italiano "
                         f"não tem o extenso entre parênteses — invariante 19")
        if c.get("fix") and dia.get("d") != 1:
            erro(f"week.json · {rotulo}: correções da auditoria só no cartão de "
                 f"segunda — invariante 14")

        rec = c.get("recall")
        if rec:
            probed = rec.get("probed", [])
            if not probed:
                erro(f"week.json · {rotulo}: há Ἀνάμνησις sem 'probed' — "
                     f"sem ele nada pode ser promovido")
            for item in probed:
                if item not in exp:
                    erro(f"week.json · {rotulo}: 'probed' cita {item!r}, que não "
                         f"está no léxico")
                elif exp[item] < 5:
                    erro(f"week.json · {rotulo}: {item!r} tem exp {exp[item]}, "
                         f"abaixo de 5 — invariante 15 proíbe testá-lo")
            if len(rec.get("prompts", [])) != len(rec.get("key", [])):
                erro(f"week.json · {rotulo}: o Ἀνάμνησις tem "
                     f"{len(rec.get('prompts', []))} prompts e "
                     f"{len(rec.get('key', []))} respostas")
            if not 2 <= len(rec.get("prompts", [])) <= 5:
                erro(f"week.json · {rotulo}: o Ἀνάμνησις tem "
                     f"{len(rec.get('prompts', []))} prompts — o limite é 2 a 5")

    validar_midia(d)


# ---------------------------------------------------------------- mídia e dados de toque
def _norm_forma(s: str) -> str:
    import unicodedata
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if not unicodedata.combining(c)).lower().replace("ς", "σ")
    return re.sub(r"[.,·;:]", "", s)


def validar_midia(d: dict) -> None:
    """Confere o que a página precisa para o card ao toque, o áudio, as fotos e os mapas."""
    fotos = (d.get("media") or {}).get("photos") or {}
    for chave, f in fotos.items():
        for campo in ("file", "alt", "expl", "cred"):
            if not f.get(campo):
                erro(f"week.json · media.photos.{chave}: falta {campo!r} — foto sem "
                     f"crédito e sem explicação não entra (invariante 23)")
        if f.get("file") and not (ROOT / "docs" / "media" / f["file"]).exists():
            erro(f"week.json · media.photos.{chave}: docs/media/{f['file']} não existe")

    def exige_foto(chave: str, onde: str) -> None:
        if chave not in fotos:
            erro(f"week.json · {onde}: cita a foto {chave!r}, que não está em media.photos")

    def exige_audio(arq: str, onde: str) -> None:
        if not (ROOT / "docs" / "audio" / arq).exists():
            erro(f"week.json · {onde}: docs/audio/{arq} não existe")

    g = d.get("greek", {})
    frases = g.get("sentences", [])
    glos = {_norm_forma(k) for k in (g.get("glossary") or {})}
    for k, v in (g.get("glossary") or {}).items():
        if not (isinstance(v, list) and len(v) == 2 and all(isinstance(x, str) and x for x in v)):
            erro(f"week.json · greek.glossary[{k!r}]: esperado [glosa, transliteração]")
    for k in (g.get("notes") or {}):
        v = g["notes"][k]
        if not (isinstance(v, list) and len(v) == 2 and isinstance(v[0], str)):
            erro(f"week.json · greek.notes[{k!r}]: esperado [dica, ver mais]")
    for k, ch in (g.get("photos") or {}).items():
        exige_foto(ch, f"greek.photos[{k!r}]")
    if g.get("glossary") is not None:
        for i, fr in enumerate(frases, 1):
            for glosa, grego, tr in fr:
                if glosa is None and _norm_forma(grego) not in glos:
                    erro(f"week.json · frase {i}: {grego!r} está sem apoio e não tem "
                         f"entrada em greek.glossary — o card ao toque ficaria vazio")
    au = (d.get("audio") or {}).get("greek")
    if au:
        exige_audio(au.get("file", ""), "audio.greek")
        if len(au.get("sent", [])) != len(frases) or len(au.get("t", [])) != len(frases):
            erro("week.json · audio.greek: sent e t precisam ter uma entrada por frase")
        else:
            for i, fr in enumerate(frases, 1):
                if len(au["t"][i - 1]) != len(fr):
                    erro(f"week.json · audio.greek.t: a frase {i} tem {len(fr)} palavras "
                         f"e {len(au['t'][i - 1])} tempos")
        for k, arq in (au.get("words") or {}).items():
            exige_audio(arq, f"audio.greek.words[{k!r}]")

    for dia in d.get("days", []):
        rot = dia.get("label", dia.get("d"))
        for c in dia.get("cards", []):
            for v in c.get("viz") or []:
                if v.get("kind") == "map":
                    if v.get("base") not in ("atica", "italia"):
                        erro(f"week.json · {rot}: mapa com base {v.get('base')!r}; "
                             f"as bases são atica e italia (page/geo.json)")
                    for pt in v.get("points", []):
                        if not all(k in pt for k in ("n", "lat", "lon")):
                            erro(f"week.json · {rot}: ponto do mapa sem n/lat/lon: {pt}")
                elif v.get("kind") == "timeline":
                    esc_ = v.get("scale")
                    for it in v.get("items", []):
                        if not (it.get("y") and it.get("t")) or (
                                ("yr" not in it) if esc_ else ("x" not in it)):
                            erro(f"week.json · {rot}: item da linha do tempo incompleto: {it}")
                else:
                    erro(f"week.json · {rot}: viz de tipo {v.get('kind')!r}; "
                         f"aceitos: map e timeline")
                if not v.get("title"):
                    erro(f"week.json · {rot}: viz sem título")
            if c.get("lang") not in ("it", "en") or not (c.get("audio") or c.get("tap")):
                continue
            if c["lang"] == "it":
                textos = [c.get("text", "")]
            else:
                textos = c.get("body", [])
            if any("<" in str(t) for t in textos):
                erro(f"week.json · {rot}: texto com marcação ({c['lang']}) — com áudio ou "
                     f"card ao toque o texto é puro, sem HTML")
            n = sum(len(str(t).split()) for t in textos)
            if c.get("audio"):
                exige_audio(c["audio"].get("file", ""), f"{rot} · audio ({c['lang']})")
                if len(c["audio"].get("t", [])) != n:
                    erro(f"week.json · {rot}: audio.t tem {len(c['audio'].get('t', []))} "
                         f"tempos para {n} palavras")
            tap = c.get("tap") or {}
            for p, v in (tap.get("p") or {}).items():
                if len(v) > 2:
                    exige_foto(v[2], f"{rot} · tap.p[{p!r}]")
            for p, ch in (tap.get("f") or {}).items():
                exige_foto(ch, f"{rot} · tap.f[{p!r}]")
            if tap:
                # toda palavra do texto abre um card: glosa em `w` ou dentro de uma `p`
                nk = lambda x: re.sub(r"[^\w'-]", "", x.lower().replace("\u2019", "'"))
                cobertas = {nk(k) for k in (tap.get("w") or {})}
                for k in (tap.get("p") or {}):
                    cobertas |= {nk(x) for x in k.split()}
                falta = sorted({nk(t) for tx in textos for t in str(tx).split()
                                if nk(t)} - cobertas)
                if falta:
                    erro(f"week.json · {rot}: palavras sem glosa em tap ({c['lang']}): "
                         f"{', '.join(falta)}")


# ---------------------------------------------------------------- manifesto
IGNORAR = {".git", ".github", "docs", "__pycache__", ".DS_Store"}


def validar_manifesto() -> None:
    p = ROOT / "README.md"
    if not p.exists():
        erro("README.md não existe")
        return
    texto = p.read_text(encoding="utf-8")
    # Só conta o que está DENTRO da tabela do manifesto. Citar um arquivo na
    # prosa não é nomeá-lo — era o que a invariante 25 quer impedir.
    secao = re.search(r"^## Manifesto\n(.*?)(?=^## )", texto, re.S | re.M)
    if not secao:
        erro("README.md não tem a seção '## Manifesto'")
        return
    listados = set(re.findall(r"`([A-Za-z0-9_./-]+\.(?:md|json|py|html))`",
                              secao.group(1)))

    no_disco = set()
    for f in ROOT.rglob("*"):
        if not f.is_file():
            continue
        rel = f.relative_to(ROOT)
        if rel.parts[0] in IGNORAR or rel.name.startswith("."):
            continue
        no_disco.add(str(rel))

    for f in sorted(no_disco - listados):
        erro(f"manifesto · {f} existe mas não aparece no README — invariante 25")
    for f in sorted(listados - no_disco):
        if f.split("/")[0] in IGNORAR:
            continue
        if not (ROOT / f).exists():
            aviso(f"manifesto · o README cita {f}, que não existe no repositório")


# ---------------------------------------------------------------- estado
def validar_logbook() -> None:
    p = ROOT / "state" / "logbook.md"
    if not p.exists():
        erro("state/logbook.md não existe")
        return
    bloco = re.search(r"```\n(.*?)```", p.read_text(encoding="utf-8"), re.S)
    if not bloco:
        erro("state/logbook.md não tem bloco de dados cercado por ```")
        return
    linhas = [l for l in bloco.group(1).splitlines() if l.strip()]
    if len(linhas) > 60:
        erro(f"state/logbook.md · {len(linhas)} linhas de dados, o máximo é 60 "
             f"— invariante 4")
    for campo in ("UPDATED", "DAY", "probed"):
        if not re.search(rf"^{campo}:", bloco.group(1), re.M):
            erro(f"state/logbook.md · falta o campo {campo}")


# MÓDULO:FALA início
def validar_fala() -> None:
    """Confere o módulo de fala, SE ele existir.

    O módulo é opcional. Apagar a pasta speaking/ não pode reprovar o build —
    por isso a função devolve em silêncio quando ela não está lá. Ver
    speaking/SPEAKING.md, seção "Como remover".
    """
    pasta = ROOT / "speaking"
    if not pasta.is_dir():
        return

    for nome in ("SPEAKING.md", "conversa.md", "entrevista.md", "log.md"):
        if not (pasta / nome).exists():
            erro(f"módulo fala · falta speaking/{nome} — o módulo está pela metade. "
                 f"Remova a pasta inteira ou restaure o arquivo.")

    log = pasta / "log.md"
    if not log.exists():
        return
    bloco = re.search(r"```\n(.*?)```", log.read_text(encoding="utf-8"), re.S)
    if not bloco:
        erro("speaking/log.md não tem bloco de dados cercado por ```")
        return
    for linha in bloco.group(1).splitlines():
        linha = linha.strip()
        if not linha or linha.startswith("FORMAT:"):
            continue
        campos = [c.strip() for c in linha.split("|")]
        if len(campos) != 5:
            erro(f"speaking/log.md · linha com {len(campos)} campos, esperados 5: {linha}")
            continue
        try:
            dt.date.fromisoformat(campos[0])
        except ValueError:
            erro(f"speaking/log.md · data inválida: {campos[0]!r}")
        if campos[1] not in ("en", "it"):
            erro(f"speaking/log.md · trilha {campos[1]!r} — só en e it têm sessão de fala")
# MÓDULO:FALA fim


def main() -> int:
    exp = ler_lexico()
    validar_semana(exp)
    validar_logbook()
    validar_manifesto()
    validar_fala()   # MÓDULO:FALA

    for a in avisos:
        print(f"aviso  · {a}")
    for e in erros:
        print(f"ERRO   · {e}", file=sys.stderr)

    if erros:
        print(f"\n{len(erros)} erro(s). O build não deve seguir.", file=sys.stderr)
        return 1
    print(f"tudo certo · {len(exp)} itens gregos no léxico"
          + (f" · {len(avisos)} aviso(s)" if avisos else ""))
    return 0


# O que este validador NÃO confere, e continua dependendo de quem compõe:
#   · se o português corrido corresponde às frases daquele dia;
#   · se toda palavra grega do texto está no léxico (as formas são flexionadas
#     e não há lematizador aqui);
#   · acentuação, aumento, aspecto, concordância;
#   · exatidão histórica.
# Ver "Controle de qualidade" em courses/GREEK_COURSE.md.

if __name__ == "__main__":
    raise SystemExit(main())
