# Hajduk Stats — SEO Pack
## hajdukstats.com | Finalna verzija · Ožujak 2026

---

## 📁 SADRŽAJ PAKETA (15 datoteka)

```
/
│  ── SLIKE ──────────────────────────────────────────────────
├── og-image.png           1200×630  Facebook, WhatsApp, LinkedIn share
├── twitter-image.png      1200×630  Twitter/X card
├── favicon.png            64×64     Browser tab (glavni)
├── favicon-32x32.png      32×32     Browser tab
├── favicon-16x16.png      16×16     Browser tab mali
├── apple-touch-icon.png   180×180   iPhone/iPad bookmark
├── icon-192.png           192×192   Android PWA ikona
├── icon-512.png           512×512   PWA splash screen
│
│  ── TEKSTUALNE DATOTEKE ─────────────────────────────────────
├── seo_head_only.html     ← novi <head> blok — kopiraj u index.html
├── robots.txt             ← upute za Google/Bing botove
├── sitemap.xml            ← mapa stranice
├── site.webmanifest       ← PWA manifest
├── _headers               ← Netlify HTTP headeri + cache
├── _redirects             ← redirect hajdukstats.com → www.hajdukstats.com
│
└── README.md              ← ove upute
```

---

## 🚀 DEPLOY KORACI

### 1. Ažuriraj index.html
Otvori `index.html` → pronađi `<head>` → zamijeni cijeli blok
sadržajem iz `seo_head_only.html`.

### 2. Dodaj Google Search Console verifikaciju
U `seo_head_only.html` postoji placeholder:
```html
<!-- <meta name="google-site-verification" content="TVOJ_NOVI_KOD_OVDJE"> -->
```
→ Idi na Search Console → dodaj property `https://www.hajdukstats.com/`
→ Kopiraj meta tag koji ti daju → odkomentiraj i zalijepi kod

### 3. Sve datoteke u GitHub root folder
```
repo/
├── index.html
├── googleXXXXXXXXXXXXXXXX.html   ← nova GSC verifikacijska datoteka
├── og-image.png
├── twitter-image.png
├── favicon.png
├── favicon-32x32.png
├── favicon-16x16.png
├── apple-touch-icon.png
├── icon-192.png
├── icon-512.png
├── robots.txt
├── sitemap.xml
├── site.webmanifest
├── _headers
└── _redirects
```

### 4. Netlify — poveži domenu
Netlify → Site Settings → Domain Management:
- Dodaj custom domain: `hajdukstats.com`
- Netlify će automatski dodati i `www.hajdukstats.com`
- Uključi **Force HTTPS**
- DNS: postavi A record ili CNAME prema Netlify uputama

### 5. Submit sitemap u Search Console
`https://www.hajdukstats.com/sitemap.xml`

---

## ⚠️ VAŽNO — www vs non-www

Odlučili smo za **www.hajdukstats.com** kao kanonsku domenu.
Datoteka `_redirects` automatski preusmjerava:
`hajdukstats.com` → `www.hajdukstats.com` (301 permanent redirect)

Ovo je važno za SEO — Google ne smije vidjeti isti sadržaj
na dvije URL adrese.

---

## ✅ PROVJERA NAKON DEPLOYA

| Alat | URL | Što provjeriš |
|------|-----|---------------|
| OG Debugger | developers.facebook.com/tools/debug/ | Izgled WhatsApp/FB sharea |
| Twitter Validator | cards-dev.twitter.com/validator | Twitter card |
| Rich Results | search.google.com/test/rich-results | FAQ schema, Breadcrumbs |
| PageSpeed | pagespeed.web.dev | Brzina (cilj: 85+ mob) |
| Search Console | search.google.com/search-console | Indexiranost |

---

*Hajduk Stats · hajdukstats.com · Ožujak 2026*
