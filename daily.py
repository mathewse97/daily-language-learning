#!/usr/bin/env python3
"""A entrega diária. Determinística — não precisa de modelo nenhum.

Faz três coisas, nesta ordem:
  1. lê o cartão de grego de hoje em state/week.json;
  2. atualiza state/logbook.md: UPDATED, DAY, probed e o "dia N/7" da lição;
  3. chama build.py, que regera docs/index.html.

Tudo o que exige julgamento — compor o grego, promover vocabulário, decidir
fase — é do planejador semanal, que é conversa com um agente e não roda aqui.
Ver TASK_PROMPTS.md.

Uso:  python3 daily.py [AAAA-MM-DD]
"""
import datetime as dt
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent
LOGBOOK = ROOT / "state" / "logbook.md"
WEEK = ROOT / "state" / "week.json"

# 0 = domingo, como no getDay() do navegador e no campo `d` do pacote.
ORDEM = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 0: 7}


def main() -> int:
    hoje = (dt.date.fromisoformat(sys.argv[1]) if len(sys.argv) > 1
            else dt.date.today())
    dow = (hoje.weekday() + 1) % 7  # segunda=1 … domingo=0

    semana = json.loads(WEEK.read_text(encoding="utf-8"))
    dia = next((d for d in semana.get("days", []) if d.get("d") == dow), None)
    if dia is None:
        print(f"erro: week.json não tem o dia {dow} ({hoje:%A})", file=sys.stderr)
        print("O planejador não compôs esta semana. Nada foi alterado.",
              file=sys.stderr)
        return 1

    cartao = next((c for c in dia.get("cards", []) if c.get("lang") == "gr"), {})
    probed = cartao.get("recall", {}).get("probed") or []
    probed_txt = ", ".join(probed) if probed else "—"

    texto = LOGBOOK.read_text(encoding="utf-8")
    anterior = re.search(r"^UPDATED: (\S+)", texto, re.M)
    ja_rodou_hoje = bool(anterior) and anterior.group(1) == hoje.isoformat()

    def campo(nome: str, valor: str, s: str) -> str:
        novo, n = re.subn(rf"^{nome}: .*$", f"{nome}: {valor}", s, count=1,
                          flags=re.M)
        if n != 1:
            print(f"aviso: campo {nome} não encontrado no logbook", file=sys.stderr)
        return novo

    texto = campo("UPDATED", hoje.isoformat(), texto)
    texto = campo("probed", probed_txt, texto)

    if not ja_rodou_hoje:
        m = re.search(r"^DAY: (\d+)", texto, re.M)
        if m:
            texto = campo("DAY", str(int(m.group(1)) + 1), texto)

    # Só o "dia N/7" da linha da lição muda; o resto dela é do planejador.
    texto = re.sub(r"dia \d/7", f"dia {ORDEM[dow]}/7", texto)

    LOGBOOK.write_text(texto, encoding="utf-8")
    print(f"logbook atualizado · {hoje} · dia {ORDEM[dow]}/7 · probed: {probed_txt}")

    return subprocess.call([sys.executable, str(ROOT / "build.py")])


if __name__ == "__main__":
    raise SystemExit(main())
