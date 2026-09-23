#!/usr/bin/env python3
"""Gera docs/index.html a partir de state/week.json e page/template.html.

A página é derivada. Nunca se edita docs/index.html à mão: edita-se o JSON e
roda-se este script. Ver PAGE_TEMPLATE.md.

Uso:  python3 build.py
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent
WEEK = ROOT / "state" / "week.json"
TEMPLATE = ROOT / "page" / "template.html"
OUT = ROOT / "docs" / "index.html"
MARKER = "__WEEK_JSON__"


def main() -> int:
    if not WEEK.exists():
        print(f"erro: {WEEK} não existe", file=sys.stderr)
        return 1
    if not TEMPLATE.exists():
        print(f"erro: {TEMPLATE} não existe", file=sys.stderr)
        return 1

    raw = WEEK.read_text(encoding="utf-8")
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"erro: state/week.json não é JSON válido — {e}", file=sys.stderr)
        return 1

    template = TEMPLATE.read_text(encoding="utf-8")
    if MARKER not in template:
        print(f"erro: {TEMPLATE} não contém {MARKER}", file=sys.stderr)
        return 1

    # json.dumps normaliza o bloco e garante que o que vai para a página é
    # exatamente o que o validador aprovou.
    payload = json.dumps(data, ensure_ascii=False, indent=2)
    html = template.replace(MARKER, payload)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    previous = OUT.read_text(encoding="utf-8") if OUT.exists() else None
    if previous == html:
        print("docs/index.html já está atualizado — nada a fazer")
        return 0

    OUT.write_text(html, encoding="utf-8")
    print(f"docs/index.html gerado · semana {data.get('week')} · "
          f"{len(data.get('days', []))} dias · {len(html)} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
