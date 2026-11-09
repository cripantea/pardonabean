#!/usr/bin/env python3
"""
Ritratti dei Guardiani — ritaglia ogni fagiolo dalla fotografia del conclave,
lo scontorna dal tovagliolo e lo deposita su fondo carta, con inquadratura
identica per tutti e dieci.

    python3 tools/ritratti.py            # rigenera tutti
    python3 tools/ritratti.py bud josef  # solo alcuni

Richiede Pillow.  Le coordinate sono le stesse di _includes/conclave-mappa.html
ed esprimono il centro del fagiolo in percentuale di conclave-mappa.jpg.
"""
from PIL import Image, ImageFilter
from collections import deque
import os
import sys

SORGENTE = "assets/img/conclave-mappa.jpg"
USCITA = "assets/img/ritratti"
CARTA = (250, 248, 245)          # --carta del foglio di stile
LATO = 560                        # lato del ritratto finale, in pixel
MARGINE = 0.17                    # aria intorno al fagiolo, in frazioni del lato

# Soglie dello scontorno, scelte confrontando i provini: il fagiolo e' bruno
# (rosso nettamente sopra il blu) e piu' scuro del tovagliolo; l'ombra portata
# resta fuori perche' e' chiara.  L'ombra viene poi ridisegnata in CSS, uguale
# per tutti, invece di essere ritagliata storta dalla fotografia.
ROSSO_MENO_BLU = 40
LUMINOSITA_MAX = 190
DILATAZIONE = 5                   # recupera il bordo morbido del fagiolo
MEDIANA = 13                      # toglie la scalettatura dal contorno

BEANS = {
    "bud":          (59.8, 46.0),
    "mata-hari":    (25.0, 34.0),
    "toto":         (38.0, 53.8),
    "don-vito":     (76.2, 42.0),
    "josef":        (36.5, 24.5),
    "ugo-fantocci": (63.5, 25.0),
    "onofrio":      (71.5, 57.5),
    "don-matteo":   (34.8, 74.2),
    "mary-poppins": (53.0, 31.5),
    "patrocle":     (57.3, 69.3),
}


def _macchia_centrale(crop):
    """Maschera del solo fagiolo al centro del ritaglio."""
    w, h = crop.size
    p = crop.load()
    binaria = Image.new("L", (w, h), 0)
    bp = binaria.load()
    for y in range(h):
        for x in range(w):
            R, G, B = p[x, y]
            if (R - B) > ROSSO_MENO_BLU and (R + G + B) / 3 < LUMINOSITA_MAX:
                bp[x, y] = 255
    d = binaria.load()

    sx, sy = w // 2, h // 2
    if not d[sx, sy]:                      # il centro puo' cadere su una macchia scura
        migliore = 10 ** 9
        for y in range(h):
            for x in range(w):
                if d[x, y]:
                    q = (x - w // 2) ** 2 + (y - h // 2) ** 2
                    if q < migliore:
                        migliore, sx, sy = q, x, y

    visti = bytearray(w * h)
    inizio = sy * w + sx
    visti[inizio] = 1
    coda = deque([inizio])
    componente = [inizio]
    while coda:
        i = coda.popleft()
        x, y = i % w, i // w
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < w and 0 <= ny < h:
                j = ny * w + nx
                if d[nx, ny] and not visti[j]:
                    visti[j] = 1
                    coda.append(j)
                    componente.append(j)

    m = Image.new("L", (w, h), 0)
    mp = m.load()
    for i in componente:
        mp[i % w, i // w] = 255
    m = m.filter(ImageFilter.MaxFilter(DILATAZIONE)).filter(ImageFilter.MinFilter(3))
    m = m.filter(ImageFilter.MedianFilter(MEDIANA))
    return m.filter(ImageFilter.GaussianBlur(1.3))


def ritratto(sorgente, slug, lato=LATO):
    px, py = BEANS[slug]
    W, H = sorgente.size
    cx, cy = int(W * px / 100), int(H * py / 100)
    crop = sorgente.crop((cx - 115, cy - 115, cx + 115, cy + 115))

    m = _macchia_centrale(crop)
    x0, y0, x1, y1 = m.getbbox()
    lunghezza = max(x1 - x0, y1 - y0)
    riquadro = lunghezza + 2 * int(lunghezza * MARGINE)
    ccx, ccy = (x0 + x1) // 2, (y0 + y1) // 2
    finestra = (ccx - riquadro // 2, ccy - riquadro // 2,
                ccx + riquadro // 2, ccy + riquadro // 2)

    fagiolo = crop.crop(finestra).resize((lato, lato), Image.LANCZOS)
    maschera = m.crop(finestra).resize((lato, lato), Image.LANCZOS)
    fuori = Image.new("RGB", (lato, lato), CARTA)
    fuori.paste(fagiolo, (0, 0), maschera)

    os.makedirs(USCITA, exist_ok=True)
    percorso = os.path.join(USCITA, slug + ".jpg")
    fuori.save(percorso, quality=92)
    return percorso, (x1 - x0, y1 - y0)


if __name__ == "__main__":
    richiesti = sys.argv[1:] or list(BEANS)
    sconosciuti = [s for s in richiesti if s not in BEANS]
    if sconosciuti:
        sys.exit("Guardiani sconosciuti: " + ", ".join(sconosciuti))
    sorgente = Image.open(SORGENTE).convert("RGB")
    for slug in richiesti:
        percorso, misura = ritratto(sorgente, slug)
        print("%-14s %s  (fagiolo %dx%d px nel ritaglio)" % (slug, percorso, *misura))
