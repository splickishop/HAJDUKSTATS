# Hajduk Stats — SEO Pack | Deploy Upute
## Finalna verzija · Ožujak 2026

---

## 📁 SADRŽAJ PAKETA

```
hajduk_seo_pack/
│
│  ── SLIKE (sve idu u root folder) ──
├── og-image.png          1200×630px  Facebook, WhatsApp, LinkedIn, Twitter share
├── twitter-image.png     1200×630px  Twitter/X card (isti sadržaj)
├── favicon.png           64×64px     Browser tab (glavni favicon)
├── favicon-32x32.png     32×32px     Browser tab
├── favicon-16x16.png     16×16px     Browser tab mali
├── apple-touch-icon.png  180×180px   iPhone/iPad bookmark ikona
├── icon-192.png          192×192px   Android PWA ikona
├── icon-512.png          512×512px   PWA splash screen
│
│  ── TEKSTUALNE DATOTEKE ──
├── seo_head_only.html               ← NOVI <head> blok za kopirati u index.html
├── robots.txt                       ← Upute za Google/Bing botove
├── sitemap.xml                      ← Mapa stranice za search engine
├── site.webmanifest                 ← PWA manifest (instalacija s mobitela)
├── _headers                         ← Netlify HTTP headeri (security + cache)
├── patch_seo.py                     ← Python skript za automatski patch
│
└── README.md                        ← Ove upute
```

---

## 🚀 DEPLOY — 3 NAČINA

### Način 1 — Ručno (preporučeno, 5 min)

1. Otvori svoju `index.html` u editoru (VS Code, Notepad++...)
2. Pronađi `<head>` — obriši SVE između `<head>` i `</head>` (uključujući oba taga)
3. Kopiraj cijeli sadržaj iz `seo_head_only.html` i zalijepi umjesto toga
4. Sve ostale datoteke iz ovog paketa postavi u **root folder** projekta

### Način 2 — Python auto-patch

```bash
# 1. Preimenuj svoju HTML datoteku
mv tvoja_datoteka.html hajduk_stats_original.html

# 2. Kopiraj patch skript i seo_head_only.html u isti folder
# 3. Pokreni
python3 patch_seo.py

# Izlaz: index.html (gotova datoteka)
```

### Način 3 — Netlify Drag & Drop

1. Otvori https://app.netlify.com → tvoj site
2. Deploys → "Drag and drop your site output folder here"
3. Ubaci folder sa svim datotekama

---

## 📂 FINALNA STRUKTURA ROOT FOLDERA

```
/  (root — što Netlify vidi)
├── index.html              ← tvoja app s novim <head>
├── robots.txt              ✅ iz ovog paketa
├── sitemap.xml             ✅ iz ovog paketa
├── site.webmanifest        ✅ iz ovog paketa
├── _headers                ✅ iz ovog paketa
├── og-image.png            ✅ iz ovog paketa
├── twitter-image.png       ✅ iz ovog paketa
├── favicon.png             ✅ iz ovog paketa
├── favicon-32x32.png       ✅ iz ovog paketa
├── favicon-16x16.png       ✅ iz ovog paketa
├── apple-touch-icon.png    ✅ iz ovog paketa
├── icon-192.png            ✅ iz ovog paketa
└── icon-512.png            ✅ iz ovog paketa
```

---

## ✅ NAKON DEPLOYA — Obavezni koraci

### 1. Google Search Console (5 min)
1. Idi na https://search.google.com/search-console
2. Add Property → `https://hajdukstats.netlify.app/`
3. Verifikacija: HTML tag metoda → kopiraj meta tag → zalijepi u `<head>` ispod canonical taga
4. Sitemaps → dodaj: `sitemap.xml` → Submit

### 2. Provjeri OG sliku
Testiraj kako link izgleda kada ga dijeliš:
- Facebook: https://developers.facebook.com/tools/debug/
- Twitter/X: https://cards-dev.twitter.com/validator
- LinkedIn: https://www.linkedin.com/post-inspector/
- WhatsApp: pošalji link sebi

### 3. Provjeri Structured Data
https://search.google.com/test/rich-results
→ unesi URL → trebao bi vidjeti FAQ i WebSite schema

### 4. PageSpeed Score
https://pagespeed.web.dev/
→ unesi URL → cilj: 85+ mobile, 95+ desktop

---

## 🔄 AŽURIRANJE SEZONE / KOLA

Kada promijeniš podatke u HTML-u (novo kolo, novi bodovi):

**sitemap.xml** — promijeni `<lastmod>` datum:
```xml
<lastmod>2026-03-20</lastmod>  ← datum zadnje promjene
```

**seo_head_only.html** — promijeni bodove u FAQ schema:
```json
"text": "HNK Hajduk Split ima 50 bodova nakon 26 odigranih kola..."
```

**og-image.png** — ako hoćeš ažurirati statistike na share slici,
javi se i generiramo novu u minuti.

---

## 🔑 KLJUČNE RIJEČI KOJE TARGETIRAMO

| Keyword | Volumen | Težina |
|---------|---------|--------|
| Hajduk Split statistike | Visok | Srednja |
| HNK Hajduk 2025 2026 | Srednji | Niska |
| Hajduk bodovi tablica | Srednji | Niska |
| SuperSport HNL statistike | Srednji | Srednja |
| Goncalo Garcia Hajduk | Nizak | Vrlo niska |
| Hajduk igrači golovi | Nizak | Niska |

---

*Hajduk Stats SEO Pack · hajdukstats.netlify.app · Ožujak 2026*
