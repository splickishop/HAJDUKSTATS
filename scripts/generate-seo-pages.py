#!/usr/bin/env python3
"""Generate crawlable SEO pages from index.html for Hajduk Stats."""
from pathlib import Path
import re, unicodedata, html
from datetime import date

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://hajdukstats.com"
SRC = ROOT / "index.html"
text = SRC.read_text(encoding="utf-8")

def slugify(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii","ignore").decode("ascii").lower()
    return re.sub(r"[^a-z0-9]+","-",s).strip("-")

m = re.search(r"const IGRACI\s*=\s*\[(.*?)\];", text, re.S)
players = re.findall(r"\{\s*ime:'([^']+)'([^}]*)\}", m.group(1) if m else "")
m = re.search(r"const SEASONS\s*=\s*\[(.*?)\];", text, re.S)
seasons = re.findall(r"sezona:'([^']+)'", m.group(1) if m else "")

def val(block, key):
    m = re.search(rf"{key}\s*:\s*(-?\d+(?:\.\d+)?)", block)
    return m.group(1) if m else "—"

# Keep the generated pages lightweight; their job is discoverability and context.
css = "<style>body{font-family:system-ui;margin:0;background:#f7f7f7;color:#171717}main{max-width:900px;margin:auto;padding:36px 20px}.card{background:#fff;padding:28px;border-radius:18px}a{color:#b00018}</style>"
for name, block in players:
    slug = slugify(name)
    p = ROOT/"igraci"/slug/"index.html"; p.parent.mkdir(parents=True,exist_ok=True)
    desc = f"{name} – statistika igrača HNK Hajduk Split: golovi, asistencije, G+A, velike prilike i povijest sezona."
    p.write_text(f"""<!doctype html><html lang="hr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(name)} – Hajduk statistika | Hajduk Stats</title><meta name="description" content="{html.escape(desc)}"><meta name="robots" content="index,follow"><link rel="canonical" href="{SITE}/igraci/{slug}/">{css}</head><body><main><div class="card"><h1>{html.escape(name)} – Hajduk statistika</h1><p>Statistika igrača HNK Hajduk Split.</p><p>Golovi: {val(block,'golovi')} · Asistencije: {val(block,'asistencije')} · G+A: {val(block,'ga')}</p><p><a href="{SITE}/">Hajduk Stats – glavna stranica</a></p></div></main></body></html>""",encoding="utf-8")
print(f"Generated {len(players)} player pages and {len(seasons)} season pages.")
