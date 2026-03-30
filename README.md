# ⚽ Hajduk Stats

**Statistička analiza HNK Hajduk Split — live podaci, pregledi po sezonama, igračima i trenerima.**

🌐 **[www.hajdukstats.com](https://www.hajdukstats.com)**

---

## O projektu

Hajduk Stats je single-page web aplikacija koja prikazuje detaljne statističke podatke o HNK Hajduk Split u SuperSport HNL-u. Podaci se automatski osvježavaju svakih 30 sekundi iz Google Apps Scripta koji čita Google Sheets.

### Sekcije

| Tab | Sadržaj |
|-----|---------|
| **Pregled** | Ključne statistike sezone, bodovi, golovi, VP/ZVP, forme |
| **Utakmice** | Sve odigrane utakmice, rezultati, strijelci |
| **Sezone** | Usporedba po sezonama (bodovi, golovi, VP) |
| **Treneri** | Statistike po trenerima (pobjede, remiji, porazi) |
| **Igrači** | Golovi, asistencije, propuštene prilike |
| **YouTube** | Preporučeni YouTube kanali o Hajduku |

---

## Tehnologije

- **Frontend:** Vanilla HTML/CSS/JavaScript (no frameworks)
- **Font:** [Comfortaa](https://fonts.google.com/specimen/Comfortaa) via Google Fonts
- **Analytics:** Google Analytics 4 (`G-MLLW3G75DX`)
- **Live data:** Google Apps Script → Google Sheets → REST API (polling svakih 30s)
- **Hosting:** GitHub Pages / prilagođena domena

---

## Struktura projekta

```
hajdukstats/
├── index.html        # Glavna (i jedina) stranica
├── sitemap.xml       # SEO sitemap
├── robots.txt        # Direktive za crawlere
├── og-image.png      # Open Graph slika (1200×630 px) — dodati ručno
├── favicon.png       # Favicon (32×32 px) — dodati ručno
├── apple-touch-icon.png  # iOS ikona (180×180 px) — dodati ručno
└── README.md         # Ovaj dokument
```

---

## Postavljanje na GitHub Pages

### 1. Klonirati repozitorij
```bash
git clone https://github.com/YOUR_USERNAME/hajdukstats.git
cd hajdukstats
```

### 2. Pokrenuti lokalno (opcionalno)
```bash
# Python 3
python -m http.server 8000
# Otvoriti: http://localhost:8000
```

### 3. Deploy na GitHub Pages
1. Idi na **Settings → Pages**
2. Source: **Deploy from a branch**
3. Branch: `main` / `(root)`
4. Spremi

### 4. Prilagođena domena
1. U Settings → Pages → Custom domain upiši: `www.hajdukstats.com`
2. Kod svog DNS providera dodaj CNAME zapis:
   ```
   CNAME  www  YOUR_USERNAME.github.io
   ```
3. Za root domenu (`hajdukstats.com`) dodaj A zapise:
   ```
   A  @  185.199.108.153
   A  @  185.199.109.153
   A  @  185.199.110.153
   A  @  185.199.111.153
   ```
4. Uključi **Enforce HTTPS** u Settings

---

## SEO

Stranica je optimizirana za tražilice:

- ✅ Meta title, description, keywords
- ✅ Canonical URL (`https://www.hajdukstats.com/`)
- ✅ Open Graph (Facebook, WhatsApp, LinkedIn)
- ✅ Twitter/X Card (`summary_large_image`)
- ✅ JSON-LD structured data (WebSite + SportsTeam schema)
- ✅ `sitemap.xml` s prioritetima i frekvencijama
- ✅ `robots.txt` s Sitemap referencom
- ✅ `lang="hr"` i `hreflang`
- ✅ Geo meta tagovi (HR-17, Split)
- ✅ `preload` za Google Fonts

### Registracija u Google Search Console
Nakon deploya registriraj stranicu na [search.google.com/search-console](https://search.google.com/search-console) i pošalji sitemap:
```
https://www.hajdukstats.com/sitemap.xml
```

---

## Slike koje treba dodati

| Datoteka | Dimenzije | Napomena |
|----------|-----------|----------|
| `og-image.png` | 1200×630 px | Slika za dijeljenje na društvenim mrežama |
| `favicon.png` | 32×32 px | Ikona u tabu preglednika |
| `apple-touch-icon.png` | 180×180 px | Ikona za iOS |

---

## Autor

Projekt razvijen s ljubavlju za Hajduk. ❤️💙

**Torcida do groba!**
