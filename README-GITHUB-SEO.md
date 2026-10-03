# Hajduk Stats — SEO + GitHub Pages

## U repository stavi
- `index.html` → sadržaj iz `hajduk-stats-GITHUB-SEO.html`
- `CNAME` → `hajdukstats.com`
- `robots.txt`
- `sitemap.xml`
- `og-image.svg`
- `igraci/`
- `sezone/`
- `scripts/generate-seo-pages.py`
- `.github/workflows/pages.yml`

## GitHub Pages
1. Repository → Settings → Pages.
2. Build and deployment → Source: **GitHub Actions**.
3. Repository → Settings → Pages → Custom domain: `hajdukstats.com`.
4. Uključi **Enforce HTTPS** kada bude dostupno.
5. Nemoj uklanjati `CNAME`.

## DNS
Za apex `hajdukstats.com` GitHub Pages koristi A zapise:
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153

Ako koristiš `www`, CNAME treba pokazivati na `<username>.github.io` prema GitHub Pages konfiguraciji.

## Google Search Console
Nakon objave:
- potvrdi `hajdukstats.com`
- pošalji `https://hajdukstats.com/sitemap.xml`
- provjeri URL Inspection za glavnu stranicu i nekoliko `/igraci/.../` URL-ova.

## Važno
`hajdukstats.com` mora biti postavljen kao Custom domain u GitHub Pages. DNS promjene mogu potrajati, a HTTPS certifikat se izdaje nakon ispravne konfiguracije.
