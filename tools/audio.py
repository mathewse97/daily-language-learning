#!/usr/bin/env python3
"""Gera o áudio da semana (voz sintética, Kokoro) e grava os tempos em state/week.json.

Roda no domingo, depois de o grego, o italiano e o inglês estarem escritos e antes do
`validate.py`. Não roda no GitHub Actions: precisa dos modelos, que não moram no repositório.

O que gera, em docs/audio/ (os arquivos de semanas antigas são apagados):
  · uma faixa com as frases gregas, mais um clipe por palavra;
  · uma faixa por texto de italiano e de inglês;
  · em state/week.json: `audio.greek`, e `audio` em cada cartão de italiano e inglês
    que tem texto (formas em WEEK_PACKET_SCHEMA.md).

Vozes: grego — a voz `em_alex` lendo fonemas do ático restaurado; italiano — `im_nicola`;
inglês — `am_michael`. O grego é a reconstrução acadêmica aproximada que o espeak-ng
oferece (voz `grc`) com as correções do curso (aspiradas, ζ = zd, ditongos longos com iota):
voz sintética de uma língua que ninguém ouviu, não áudio atestado. A página diz isso.

Preparação, uma vez:
  pip install kokoro-onnx espeakng-loader numpy      (e ffmpeg no PATH)
  kokoro-v1.0.onnx, kokoro-v1.0.int8.onnx e voices-v1.0.bin, das releases de
  github.com/thewh1teagle/kokoro-onnx, numa pasta qualquer.

Uso:  python3 tools/audio.py --modelos PASTA [--libs PASTA_COM_OS_PACOTES]
"""
import argparse
import ctypes
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
WEEK = ROOT / "state" / "week.json"
OUT = ROOT / "docs" / "audio"
SR = 24000
FIM = re.compile(r"[.?!][»”\"]?$")


def args():
    p = argparse.ArgumentParser()
    p.add_argument("--modelos", required=True, help="pasta com os .onnx e voices-v1.0.bin")
    p.add_argument("--libs", help="pasta com pacotes Python a acrescentar ao sys.path")
    return p.parse_args()


def mp3(np, samples, dest, kbps=24):
    pcm = (np.clip(samples, -1, 1) * 32767).astype("<i2").tobytes()
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "s16le", "-ar", str(SR), "-ac", "1",
                    "-i", "-", "-af", "loudnorm=I=-18", "-ar", str(SR), "-b:a", f"{kbps}k", str(dest)],
                   input=pcm, check=True)


# ---------------------------------------------------------------- grego: fonemas
def fonemas_gregos():
    import espeakng_loader as L
    e = ctypes.CDLL(L.get_library_path())
    e.espeak_Initialize(0x0002, 0, L.get_data_path().encode(), 0)
    e.espeak_SetVoiceByName(b"grc")
    e.espeak_TextToPhonemes.restype = ctypes.c_char_p

    def fon(txt):
        b = ctypes.c_char_p(txt.encode("utf-8"))
        ptr = ctypes.pointer(b)
        out = []
        while ptr.contents.value:
            r = e.espeak_TextToPhonemes(ptr, 1, 2)
            if not r:
                break
            out.append(r.decode())
        return " ".join(out)

    def atico(ipa):
        ipa = ipa.replace("_", "")
        ipa = ipa.replace("ɛɪː", "ɛːi").replace("aɪː", "aːi").replace("ɔɪː", "ɔːi")
        ipa = ipa.replace("ɪ", "i").replace("ʊ", "u")
        ipa = ipa.replace("f", "pʰ").replace("θ", "tʰ").replace("x", "kʰ")
        ipa = re.sub(r"z(?!d)", "zd", ipa)
        return re.sub(r"\s+", " ", ipa).strip()
    return lambda txt: atico(fon(txt))


# ---------------------------------------------------------------- síntese
def main() -> int:
    a = args()
    if a.libs:
        sys.path.insert(0, a.libs)
    import numpy as np
    from kokoro_onnx import Kokoro
    mod = pathlib.Path(a.modelos)
    leve = Kokoro(str(mod / "kokoro-v1.0.int8.onnx"), str(mod / "voices-v1.0.bin"))
    cheio = Kokoro(str(mod / "kokoro-v1.0.onnx"), str(mod / "voices-v1.0.bin"))
    sil = lambda s: np.zeros(int(SR * s), dtype=np.float32)

    def frase(model, voz, vel, lang, itens, fon=False):
        """itens = [(exibido, falado|None)]; devolve (amostras, início de cada item em s)."""
        sp = [s for _, s in itens if s]
        D, last = [0.0], None
        for k in range(1, len(sp) + 1):
            x, _ = model.create(" ".join(sp[:k]), voice=voz, speed=vel, lang=lang, is_phonemes=fon, trim=False)
            D.append(len(x) / SR)
            last = x
        ini, j = [], 0
        for _, s in itens:
            if s:
                ini.append(max(0.0, D[j] - 0.06))
                j += 1
            else:
                ini.append(None)
        nxt = None
        for i in range(len(ini) - 1, -1, -1):
            if ini[i] is None:
                ini[i] = nxt if nxt is not None else D[-1]
            else:
                nxt = ini[i]
        return last, ini

    def partes(tokens):
        out, cur = [], []
        for t in tokens:
            cur.append(t)
            if FIM.search(t[0]):
                out.append(cur)
                cur = []
        if cur:
            out.append(cur)
        return out

    def faixa(model, voz, vel, lang, paragrafos, nome):
        amostras, tempos, t = [], [], 0.0
        for par in paragrafos:
            ps = partes(par)
            for si, s in enumerate(ps):
                x, ini = frase(model, voz, vel, lang, s)
                amostras.append(x)
                tempos += [round(t + v, 2) for v in ini]
                t += len(x) / SR
                g = 0.6 if si == len(ps) - 1 else 0.3
                amostras.append(sil(g))
                t += g
        mp3(np, np.concatenate(amostras), OUT / nome)
        return tempos

    week = json.loads(WEEK.read_text(encoding="utf-8"))
    n = week["week"]
    pre = f"w{n:02d}_"
    OUT.mkdir(parents=True, exist_ok=True)
    limpa = lambda w: re.sub(r"[.,·;:]", "", w)

    # ---- grego: uma faixa com as frases; cada frase é um trecho
    fon = fonemas_gregos()
    amostras, sents, tempos, t = [], [], [], 0.0
    for i, fr in enumerate(week["greek"]["sentences"]):
        pal = fon(" ".join(limpa(w[1]) for w in fr)).split()
        assert len(pal) == len(fr), f"frase {i + 1}: {len(pal)} fonemas para {len(fr)} palavras"
        x, ini = frase(cheio, "em_alex", 0.82, "es", [(w[1], p) for w, p in zip(fr, pal)], fon=True)
        amostras += [x, sil(0.7)]
        tempos.append([round(t + v, 2) for v in ini])
        sents.append([round(t, 2), round(t + len(x) / SR, 2)])
        t += len(x) / SR + 0.7
    mp3(np, np.concatenate(amostras), OUT / f"{pre}grc.mp3")
    palavras = {}
    for j, w in enumerate(dict.fromkeys(limpa(w[1]) for fr in week["greek"]["sentences"] for w in fr)):
        x, _ = cheio.create(fon(w), voice="em_alex", speed=0.78, lang="es", is_phonemes=True)
        arq = f"{pre}grc_{j:02d}.mp3"
        mp3(np, x, OUT / arq)
        palavras[w] = arq
    week.setdefault("audio", {})["greek"] = {"file": f"{pre}grc.mp3", "sent": sents, "t": tempos, "words": palavras}
    print(f"grego · {round(t, 1)} s · {len(palavras)} palavras", flush=True)

    # ---- italiano e inglês
    def tok_it(txt):
        toks, out = txt.split(), []
        for i, tk in enumerate(toks):
            if re.fullmatch(r"\d+", tk) and i + 1 < len(toks) and toks[i + 1].startswith("("):
                out.append((tk, None))      # o algarismo não é falado; o extenso entre parênteses é
                continue
            out.append((tk, re.sub(r"[()«»“”\"]", "", tk) or None))
        return out

    for d in week["days"]:
        for c in d["cards"]:
            if c["lang"] == "it" and c.get("text") and d["d"] != 0:
                arq = f"{pre}it{d['d']}.mp3"
                tempos = faixa(leve, "im_nicola", 0.95, "it", [tok_it(c["text"])], arq)
                c["audio"] = {"file": arq, "t": tempos}
                print("italiano", d["d"], len(tempos), "palavras", flush=True)
            if c["lang"] == "en" and c.get("body") and c.get("title"):
                arq = f"{pre}en{d['d']}.mp3"
                pars = [[(tk, re.sub(r"[“”\"]", "", tk) or None) for tk in p.split()] for p in c["body"]]
                tempos = faixa(leve, "am_michael", 0.97, "en-us", pars, arq)
                c["audio"] = {"file": arq, "t": tempos}
                print("inglês", d["d"], len(tempos), "palavras", flush=True)

    WEEK.write_text(json.dumps(week, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for f in OUT.glob("*.mp3"):
        if not f.name.startswith(pre):
            f.unlink()
    print("pronto: confira com validate.py e build.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
