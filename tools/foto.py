#!/usr/bin/env python3
"""Baixa uma foto livre para docs/media/ e imprime a entrada de `media.photos`.

Duas fontes, as que o curso usa:
  python3 tools/foto.py met 254872 vinho-anfora
      — The Met, só objetos com domínio público (CC0);
  python3 tools/foto.py commons "Colosseo 2020.jpg" coliseu
      — Wikimedia Commons, só licenças CC0, CC BY e CC BY-SA, com o autor.

A imagem é reduzida a 960 px de largura (JPEG). A saída é o JSON da entrada; `alt` e
`expl` ficam vazios de propósito, para o `validate.py` reprovar até alguém escrever o que
a foto mostra e por que ela está ali. O crédito já vem preenchido.

Wikimedia limita pedidos seguidos (HTTP 429): se acontecer, espere alguns minutos.
"""
import json
import pathlib
import re
import subprocess
import sys
import time
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "media"
UA = {"User-Agent": "DailyLanguageLearning/1.0 (estudo pessoal)"}
LICENCAS = ("CC0", "CC BY", "CC BY-SA", "Public domain", "PD")


def get(url: str, bruto: bool = False, tentativas: int = 4):
    for i in range(tentativas):
        try:
            dado = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read()
            return dado if bruto else json.loads(dado)
        except Exception as e:                       # 429 e quedas de rede: espera e repete
            print(f"  nova tentativa ({str(e)[:50]})", file=sys.stderr)
            time.sleep(15 * (i + 1))
    raise SystemExit("não consegui baixar: " + url)


def salvar(dado: bytes, chave: str) -> str:
    OUT.mkdir(parents=True, exist_ok=True)
    destino = OUT / f"{chave}.jpg"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", "-", "-vf", "scale='min(960,iw)':-2",
                    "-q:v", "4", str(destino)], input=dado, check=True)
    return destino.name


def met(oid: str, chave: str) -> dict:
    o = get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{oid}")
    if not o.get("isPublicDomain"):
        raise SystemExit("objeto sem domínio público: não entra")
    url = o.get("primaryImage") or o.get("primaryImageSmall")
    arq = salvar(get(url, bruto=True), chave)
    return {"file": arq, "alt": "", "expl": "",
            "cred": f"{o['title']}, {o['objectDate']}. The Metropolitan Museum of Art, domínio público.",
            "page": o["objectURL"]}


def commons(titulo: str, chave: str) -> dict:
    nome = "File:" + titulo.removeprefix("File:")
    q = ("https://en.wikipedia.org/w/api.php?action=query&format=json&prop=imageinfo"
         "&iiprop=extmetadata|url&iiurlwidth=960&titles=" + urllib.parse.quote(nome))
    pag = next(iter(get(q)["query"]["pages"].values()))
    ii = pag["imageinfo"][0]
    m = ii["extmetadata"]
    lic = m["LicenseShortName"]["value"]
    if not any(lic.startswith(l) for l in LICENCAS):
        raise SystemExit(f"licença {lic!r} não é aceita")
    autor = re.sub(r"<[^>]+>", "", m["Artist"]["value"]).strip()
    url = ii["thumburl"].split("?")[0].replace("thumb.wikimedia.org", "upload.wikimedia.org")
    arq = salvar(get(url, bruto=True), chave)
    return {"file": arq, "alt": "", "expl": "", "cred": f"Foto: {autor}, {lic}, via Wikimedia Commons.",
            "page": "https://commons.wikimedia.org/wiki/" + nome.replace(" ", "_")}


def main() -> int:
    if len(sys.argv) != 4 or sys.argv[1] not in ("met", "commons"):
        print(__doc__)
        return 2
    _, fonte, ref, chave = sys.argv
    r = met(ref, chave) if fonte == "met" else commons(ref, chave)
    print(json.dumps({chave: r}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
