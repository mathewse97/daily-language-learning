#!/usr/bin/env python3
"""Mapas e linhas do tempo como SVG, gerados a partir de dados.

O pacote da semana descreve o que desenhar (`viz` num cartão: pontos, rota, anos);
este módulo desenha. Quem compõe nunca escreve SVG. `build.py` chama `expandir()`
e põe o resultado no campo `svg` da cópia que vai para a página — o `state/week.json`
fica sem ele. O contorno vem de `page/geo.json` (Natural Earth, domínio público).

Formas aceitas em `viz` (ver WEEK_PACKET_SCHEMA.md):

  {"kind": "map", "base": "atica" | "italia", "title": "...", "cap": "...",
   "points": [{"n": "Acarnas", "lat": 38.08, "lon": 23.74, "hl": true,
               "dx": 8, "dy": -2, "a": "start"}],
   "route": [[lat, lon], ...], "hills": [[lat, lon, largura, altura]],
   "labels": [{"t": "Parnes", "lat": 38.2, "lon": 23.6, "a": "start"}]}

  {"kind": "timeline", "title": "...", "cap": "...", "scale": [510, 430],
   "items": [{"yr": 490, "y": "490", "t": "Maratona", "lvl": -1, "hl": false}]}
  Sem "scale", cada item traz "x" (0 a 1) em vez de "yr", e o eixo é só uma ordem.
"""
import copy
import html
import json
import math
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
GEO = json.loads((ROOT / "page" / "geo.json").read_text(encoding="utf-8"))


def esc(s) -> str:
    return html.escape(str(s), quote=True)


def _proj(base: dict, mx: float = 14, my: float = 12):
    la0, la1, lo0, lo1 = base["box"]
    s = base["s"]
    kx = 111.0 * math.cos(math.radians((la0 + la1) / 2))
    w = (lo1 - lo0) * kx * s + 2 * mx
    h = (la1 - la0) * 111.0 * s + 2 * my

    def p(lat: float, lon: float):
        return (round(mx + (lon - lo0) * kx * s, 1), round(my + (la1 - lat) * 111.0 * s, 1))
    return p, round(w), round(h)


def mapa(v: dict) -> str:
    base = GEO[v["base"]]
    p, w, h = _proj(base)
    s = f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="{esc(v.get("title", "Mapa"))}">'
    s += f'<rect class="sea" width="{w}" height="{h}" rx="8"/>'
    for ring in base["rings"]:
        pts = " ".join("%s,%s" % p(la, lo) for la, lo in ring)
        s += f'<polygon class="land" points="{pts}"/>'
    for la, lo, hw, hh in v.get("hills", []):
        x, y = p(la, lo)
        s += f'<path class="hill" d="M{x - hw} {y} l{hw} -{hh} l{hw} {hh}"/>'
    for lb in v.get("labels", []):
        x, y = p(lb["lat"], lb["lon"])
        s += f'<text class="lbl2" x="{x}" y="{y}" text-anchor="{lb.get("a", "start")}">{esc(lb["t"])}</text>'
    rota = v.get("route")
    if rota:
        pts = " ".join("%s,%s" % p(la, lo) for la, lo in rota)
        s += f'<polyline class="route" points="{pts}"/>'
    for pt in v.get("points", []):
        x, y = p(pt["lat"], pt["lon"])
        hl = pt.get("hl")
        r = 5 if hl else 3.6
        s += (f'<circle class="{"pt" if hl else "ptd"}" cx="{x}" cy="{y}" r="{r}"/>'
              f'<text class="{"lblb" if hl else "lbl2"}" x="{x + pt.get("dx", 7)}" '
              f'y="{y + pt.get("dy", 3)}" text-anchor="{pt.get("a", "start")}">{esc(pt["n"])}</text>')
    return s + "</svg>"


def linha_do_tempo(v: dict, w: int = 340) -> str:
    itens = v["items"]
    passo = 26 if any(abs(i.get("lvl", 1)) > 1 for i in itens) else 22
    niveis = max(abs(i.get("lvl", 1)) for i in itens)
    h = 2 * (14 + passo * niveis + 26)
    y0 = h / 2
    esc_ = v.get("scale")
    s = f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="{esc(v.get("title", "Linha do tempo"))}">'
    s += f'<line class="axis" x1="14" y1="{y0}" x2="{w - 14}" y2="{y0}"/>'
    for i in itens:
        x = (esc_[0] - i["yr"]) / (esc_[0] - esc_[1]) if esc_ else i["x"]
        px = 14 + x * (w - 28)
        lvl = i.get("lvl", 1)
        up = lvl >= 0
        y1 = y0 - (14 + passo * abs(lvl)) if up else y0 + (14 + passo * abs(lvl))
        s += f'<line class="tick" x1="{px}" y1="{y0}" x2="{px}" y2="{y1}"/>'
        s += f'<circle class="{"pt2" if i.get("hl") else "pt"}" cx="{px}" cy="{y0}" r="{5 if i.get("hl") else 3.6}"/>'
        ty = y1 - 14 if up else y1 + 14
        a = "start" if px < 60 else ("end" if px > w - 70 else "middle")
        s += f'<text class="lblb" x="{px}" y="{ty}" text-anchor="{a}">{esc(i["y"])}</text>'
        s += f'<text class="lbl2" x="{px}" y="{ty + 11}" text-anchor="{a}">{esc(i["t"])}</text>'
    return s + "</svg>"


def expandir(semana: dict) -> dict:
    """Cópia da semana com `svg` em cada item de `viz`. Não toca no original."""
    out = copy.deepcopy(semana)
    for d in out.get("days", []):
        for c in d.get("cards", []):
            for v in c.get("viz") or []:
                v["svg"] = mapa(v) if v["kind"] == "map" else linha_do_tempo(v)
                if v["kind"] == "map":
                    v["cap"] = (v.get("cap", "") + " Contorno: Natural Earth.").strip()
    return out
