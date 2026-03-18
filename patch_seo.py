#!/usr/bin/env python3
"""
Hajduk Stats — SEO Head Patch Script
Pokreni: python3 patch_seo.py
Ulaz:  hajduk_stats_original.html  (tvoja originalna datoteka)
Izlaz: index.html                  (finalna verzija)
"""
import re, sys, os

input_file = "hajduk_stats_original.html"
output_file = "index.html"

if not os.path.exists(input_file):
    print(f"GREŠKA: Ne mogu naći '{input_file}'")
    print(f"Preimenuj svoju HTML datoteku u '{input_file}' i pokušaj ponovo.")
    sys.exit(1)

with open(input_file, "r", encoding="utf-8") as f:
    html = f.read()

NEW_HEAD = open("seo_head_only.html", "r", encoding="utf-8").read()

# Replace everything between <head> and </head>
html_new = re.sub(r"<head>.*?</head>", NEW_HEAD, html, flags=re.DOTALL)

with open(output_file, "w", encoding="utf-8") as f:
    f.write(html_new)

print(f"✅ Gotovo! Spremi '{output_file}' u root folder Netlify projekta.")
