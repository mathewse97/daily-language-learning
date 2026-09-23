#!/usr/bin/env python3
"""A entrega diária. Determinística — não precisa de modelo nenhum.

Faz três coisas, nesta ordem:
  1. lê o cartão de grego de hoje em state/week.json;
  2. atualiza state/logbook.md: UPDATED, DAY, probed e o "dia N/7" da lição;
  3. chama build.py, que regera docs/index.html.

Tudo o que exige julgamento — compor o grego, promover vocabulário, decidir
fase — é do planejador semanal, que é conversa com um agente e não roda aqui.
Ver TASK_PROMPTS.md.

A data é sempre a de Brasília, não a do servidor.

Uso:  python3 daily.py [AAAA-MM-DD]
"""
import datetime as dt
import json
import pathlib
import re
import subprocess
import sys

try:
    from zoneinfo import ZoneInfo
    FUSO = ZoneInfo("America/Sao_Paulo")
except Exception:                       # runner sem base de fusos instalada
    FUSO = dt.timezone(dt.timedelta(hours=-3))

ROOT = pathlib.Path(__file__).resolve().parent
LOGBOOK = ROOT / "state" / "logbook.md"
WEEK = ROOT / "state" / "week.json"

# 0 = domingo, como no getDay() do navegador e no campo `d` do pacote.
ORDEM = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 0: 7}


def main() -> int:
    # O fuso é explícito de propósito. O runner do GitHub roda em UTC, e uma
    # execução manual depois das 21h em Brasília já é "amanhã" lá — foi assim
    # que a entrega de 22/09 gravou a data 23/09 e sobrescreveu o `probed` do
    # dia. A lição é lida no horário de Brasília; a data é a de Brasília.
    hoje = (dt.date.fromisoformat(sys.argv[1]) if len(sys.argv) > 1
            else dt.datetime.now(FUSO).date())
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
    try:
        data_anterior = dt.date.fromisoformat(anterior.group(1)) if anterior else None
    except ValueError:
        data_anterior = None
    # DAY só anda para a frente. Rodar de novo no mesmo dia, ou corrigir uma
    # data que ficou adiantada, não conta como um dia de curso a mais.
    avancar_dia = data_anterior is None or data_anterior < hoje

    def campo(nome: str, valor: str, s: str) -> str:
        novo, n = re.subn(rf"^{nome}: .*$", f"{nome}: {valor}", s, count=1,
                          flags=re.M)
        if n != 1:
            print(f"aviso: campo {nome} não encontrado no logbook", file=sys.stderr)
        return novo

    texto = campo("UPDATED", hoje.isoformat(), texto)
    texto = campo("probed", probed_txt, texto)

    if avancar_dia:
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
