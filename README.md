# Archivio Hub — landing page + QR

Landing page statica che funge da hub di orientamento per chi scansiona il QR code: due link essenziali (bot Telegram, Google Form per contributori) e una breve descrizione del progetto.

## Contenuto

```
archivio_hub/
├── index.html          # Pagina unica, HTML+CSS inline, zero dipendenze
├── generate_qr.py      # Script per generare il QR code stampabile
└── README.md           # Questo file
```

## Prerequisiti

- Account GitHub (già esistente: `archiviolvca-oss`).
- Python 3.x con `pip` per il QR code.
- I due URL definitivi: bot Telegram e Google Form.

---

## Passo 1 — Personalizzare i contenuti

Aprire `index.html` e sostituire i tre placeholder:

| Cerca | Sostituisci con |
|---|---|
| `https://t.me/IL_TUO_BOT` | URL reale del bot, es. `https://t.me/archivio_lvca_bot` |
| `https://forms.gle/IL_TUO_FORM` | URL del Google Form |
| (eventuali ritocchi a testi e tagline) | a piacere |

Tutti i testi sono in chiaro nel file, modificabili senza toccare il CSS.

---

## Passo 2 — Pubblicare su GitHub Pages

Da terminale Mac, dalla cartella del progetto:

```bash
# Inizializza il repo locale
cd archivio_hub
git init
git add .
git commit -m "Prima versione hub"

# Crea il repo su GitHub (PUBBLICO — necessario per Pages gratis)
# via web: https://github.com/new   nome suggerito: archivio-hub

# Collega il remote (sostituisci USERNAME con archiviolvca-oss)
git branch -M main
git remote add origin git@github.com:USERNAME/archivio-hub.git
git push -u origin main
```

Sul sito di GitHub:

1. Vai su **Settings > Pages** del repo.
2. Sotto **Source**, seleziona **Deploy from a branch**.
3. Scegli **Branch: `main`**, **Folder: `/ (root)`**, salva.
4. Attendi 1–2 minuti. L'URL pubblico apparirà in cima alla pagina:
   `https://USERNAME.github.io/archivio-hub/`

Verifica: apri quell'URL in incognito e controlla che i due pulsanti aprano i link giusti.

---

## Passo 3 — Generare il QR code

Una volta che la landing è online e funzionante:

```bash
# Sul Mac, dalla cartella archivio_hub
source .venv/bin/activate         # se hai un venv di progetto
pip install "qrcode[pil]"

# Apri generate_qr.py e modifica la variabile HUB_URL con l'URL reale
# (quello restituito da GitHub Pages)

python generate_qr.py
```

Output: `qr_archivio.png`, ~1700×1700 px, pronto per stampa adesivi fino a 10×10 cm.

---

## Aggiornamenti futuri

Modifiche al testo o ai link:

```bash
# Sul Mac, nella cartella del repo
# Modifica index.html, poi:
git add index.html
git commit -m "Aggiornamento testi"
git push
```

GitHub Pages ridistribuisce automaticamente in 30–60 secondi. Il QR code **non cambia** finché non cambia l'URL della pagina, quindi gli adesivi già stampati restano validi a vita.

---

## Note progettuali

- **Tipografia**: Fraunces (display, serif moderna con personalità) e Manrope (body, sans-serif sobria). Caricate da Google Fonts in `display=swap` per non bloccare il render.
- **Palette**: blu mezzanotte (`#0a1729`) su avorio caldo (`#fafaf7`). Tocco di oro tenue (`#b8945c`) per l'accento sulla parola in italico del titolo.
- **Animazioni**: fade-in scaglionato al caricamento, disabilitate automaticamente per chi ha `prefers-reduced-motion: reduce` attivo.
- **Accessibilità**: target tappabili da 56px minimo, contrasto AAA sul testo principale, `aria-hidden` sugli elementi decorativi.
- **Performance**: nessun JavaScript, file totale < 8 KB (al netto dei font esterni).

---

## Migrazione futura su Hetzner (eventuale)

Se un giorno vorrai ospitare la landing sulla VPS:

1. Registra un dominio (es. `archivio-lvca.it`).
2. Punta il record A all'IP della VM (`23.88.63.187`).
3. Installa Nginx + certbot, copia `index.html` in `/var/www/archivio-hub/`.
4. Aggiorna il QR code con il nuovo URL — gli adesivi vecchi diventeranno obsoleti.

Il punto 4 è il motivo per cui conviene rimandare la migrazione finché non c'è una vera necessità: ogni cambio di URL invalida la stampa fisica.
