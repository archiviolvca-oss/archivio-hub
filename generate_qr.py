"""
generate_qr.py
---------------
Genera un QR code ad alta risoluzione per la stampa di adesivi.

Uso:
    1. Configurare la variabile HUB_URL con l'URL della landing page
       (es. https://USERNAME.github.io/archivio-hub).
    2. Eseguire dal Mac:
           source .venv/bin/activate
           pip install qrcode[pil]
           python generate_qr.py
    3. Output: file 'qr_archivio.png' nella cartella corrente.

Note tecniche:
    - error_correction=H (~30%): tollera macchie/usura sull'adesivo.
    - box_size=40: produce un PNG di circa 1700x1700 px, abbondante per
      stampa di adesivi fino a 10x10 cm a 300 DPI.
    - border=4: quiet zone standard, indispensabile per la lettura
      affidabile dai lettori QR (non rimuovere).
"""

import qrcode
from qrcode.constants import ERROR_CORRECT_H

# === CONFIGURAZIONE =========================================================
HUB_URL = HUB_URL = "https://archiviolvca-oss.github.io/archivio-hub/"   # <-- modificare qui
OUTPUT_FILE = "qr_archivio.png"
# ============================================================================


def generate_qr(url: str, output_path: str) -> None:
    """Genera un PNG QR code in alta risoluzione."""
    qr = qrcode.QRCode(
        version=None,                  # auto: sceglie la versione minima sufficiente
        error_correction=ERROR_CORRECT_H,
        box_size=40,                   # px per modulo (cella) del QR
        border=4,                      # moduli di quiet zone (margine bianco)
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Colori coerenti con la palette della landing (blu mezzanotte su avorio)
    img = qr.make_image(fill_color="#0a1729", back_color="#fafaf7")
    img.save(output_path)

    width, height = img.size
    print(f"QR generato: {output_path}")
    print(f"Dimensioni:  {width}x{height} px")
    print(f"URL:         {url}")
    print()
    print("Suggerimento di stampa:")
    print(f"  - Adesivo 5x5 cm  -> {width / (5/2.54):.0f} DPI")
    print(f"  - Adesivo 8x8 cm  -> {width / (8/2.54):.0f} DPI")
    print(f"  - Adesivo 10x10 cm -> {width / (10/2.54):.0f} DPI")
    print("  (tutti ben sopra i 300 DPI minimi per stampa di qualità)")


if __name__ == "__main__":
    if "USERNAME" in HUB_URL:
        raise SystemExit(
            "ERRORE: sostituire 'USERNAME' nella variabile HUB_URL "
            "con il proprio username GitHub prima di eseguire."
        )
    generate_qr(HUB_URL, OUTPUT_FILE)
