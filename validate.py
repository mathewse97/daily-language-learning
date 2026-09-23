#!/usr/bin/env python3
"""Confere as invariantes que um arquivo pode conferir sozinho.

Roda em todo commit, pelo GitHub Actions, e localmente com:  python3 validate.py

O que ele NÃO confere está dito no fim deste arquivo, de propósito: um
validador que finge cobrir o que não cobre é pior que nenhum.
"""
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
        if secao.startswith("[GR"):
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


def main() -> int:
    exp = ler_lexico()
    validar_semana(exp)
    validar_logbook()
    validar_manifesto()

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
