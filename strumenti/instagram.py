#!/usr/bin/env python3
"""Genera il materiale per il profilo Instagram @pardonabean.

    python3 strumenti/instagram.py tondo
    python3 strumenti/instagram.py apertura
    python3 strumenti/instagram.py giorno <foto.jpg> "<Occhiello>" "<Titolo>" <nome-file>

Tutto finisce in social/, che non viene pubblicato dal sito.
"""
import os, sys, textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1350                      # formato verticale di Instagram
CARTA, CARTA_SCURA = "#faf8f5", "#f2eee6"
INCHIOSTRO, SOFT, BORLOTTO, BORDO = "#23251f", "#4a4d44", "#9e3b3b", "#ded8cc"
F = "/System/Library/Fonts/Supplemental/"
FUORI = "social"


def g(n, s): return ImageFont.truetype(F + n, s)
def bold(s): return g("Georgia Bold.ttf", s)
def tondo_f(s): return g("Georgia.ttf", s)
def cors(s): return g("Georgia Italic.ttf", s)


def taglia_barra(foto):
    """Elimina la fascia chiara con i dati dello scatto che il telefono stampa
    in fondo alla fotografia. Sul sito resta: contiene data e ora e fa da
    documento. Su Instagram sporca la composizione. Taglia al massimo il 6%."""
    import statistics
    g = foto.convert("L"); w, h = g.size; px = g.load()
    def misura(y):
        v = [px[x, y] for x in range(0, w, 7)]
        return statistics.median(v), statistics.pstdev(v)

    # 1. la fascia comincia con righe chiare e uniformi attaccate al bordo
    barra = 0
    for y in range(h - 1, int(h * 0.94), -1):
        m, sd = misura(y)
        if m > 200 and sd < 45:
            barra = h - y
        else:
            break
    if not barra:
        return foto
    # 2. risale attraverso le righe che contengono la scritta: restano chiare
    #    ma non sono uniformi. Senza il punto 1 non si entra mai qui, cosi' un
    #    tovagliolo chiaro in fondo alla foto non viene mai tagliato.
    for y in range(h - barra - 1, int(h * 0.88), -1):
        if misura(y)[0] > 190:
            barra = h - y
        else:
            break
    return foto.crop((0, 0, w, h - barra))


def riempi(foto, larg, alt):
    foto = taglia_barra(foto)
    """Ritaglio centrato che riempie esattamente larg x alt."""
    r = max(larg / foto.width, alt / foto.height)
    foto = foto.resize((max(1, round(foto.width * r)), max(1, round(foto.height * r))), Image.LANCZOS)
    sx, sy = (foto.width - larg) // 2, (foto.height - alt) // 2
    return foto.crop((sx, sy, sx + larg, sy + alt))


def a_capo(d, testo, font, larghezza):
    righe, riga = [], ""
    for p in testo.split():
        prova = (riga + " " + p).strip()
        if d.textlength(prova, font=font) <= larghezza:
            riga = prova
        else:
            righe.append(riga); riga = p
    if riga: righe.append(riga)
    return righe


def piede(d, x, larg, y):
    d.line([(x, y), (x + larg, y)], fill=BORDO, width=2)
    d.text((x, y + 26), "pardonabean.it", font=bold(27), fill=INCHIOSTRO)
    d.text((x + larg, y + 28), "@pardonabean", font=cors(23), fill=SOFT, anchor="ra")


# ----------------------------------------------------------- immagine profilo
def tondo():
    """Instagram ritaglia un cerchio dal centro e lo mostra a 40 pixel: il
    fagiolo deve riempire il quadro, non posarci dentro."""
    lato = 1080
    f = Image.open("assets/img/ritratti/bud.jpg").convert("RGB")
    # riquadro effettivo del fagiolo: tutto cio' che non e' fondo chiaro
    g = f.convert("L"); w, h = g.size; px = g.load()
    xs = [x for x in range(w) for y in range(0, h, 3) if px[x, y] < 215]
    ys = [y for y in range(h) for x in range(0, w, 3) if px[x, y] < 215]
    x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
    m = int(max(x1 - x0, y1 - y0) * 0.06)
    f = f.crop((max(0, x0 - m), max(0, y0 - m), min(w, x1 + m), min(h, y1 + m)))

    # largo 860: resta dentro il cerchio perche' il fagiolo e' piu' basso che largo
    largo = 860
    f = f.resize((largo, max(1, round(f.height * largo / f.width))), Image.LANCZOS)
    tela = Image.new("RGB", (lato, lato), CARTA)
    tela.paste(f, ((lato - f.width) // 2, (lato - f.height) // 2))
    os.makedirs(FUORI, exist_ok=True)
    tela.save(FUORI + "/profilo-tondo.jpg", quality=92)
    return FUORI + "/profilo-tondo.jpg"


# ------------------------------------------------------- post con fotografia
def con_foto(foto_path, occhiello, titolo, nome, dida=None):
    tela = Image.new("RGB", (W, H), CARTA)
    d = ImageDraw.Draw(tela)
    alt_foto = 880
    tela.paste(riempi(Image.open(foto_path).convert("RGB"), W, alt_foto), (0, 0))
    x, larg = 70, W - 140
    d.line([(x, alt_foto + 62), (x + 76, alt_foto + 62)], fill=BORLOTTO, width=5)
    d.text((x, alt_foto + 86), occhiello.upper(), font=bold(20), fill=BORLOTTO)
    for dim in (52, 46, 40, 35):
        f = bold(dim); righe = a_capo(d, titolo, f, larg)
        if len(righe) <= 2: break
    y = alt_foto + 140
    for r in righe:
        d.text((x, y), r, font=f, fill=INCHIOSTRO); y += int(dim * 1.2)
    if dida:
        for r in a_capo(d, dida, tondo_f(25), larg)[:2]:
            d.text((x, y + 10), r, font=tondo_f(25), fill=SOFT); y += 34
    piede(d, x, larg, H - 112)
    os.makedirs(FUORI, exist_ok=True)
    p = "%s/%s.jpg" % (FUORI, nome)
    tela.save(p, quality=90, optimize=True)
    return p


# ------------------------------------------------------ post di solo testo
def manifesto(occhiello, titolo, corpo, nome, cifra=None):
    tela = Image.new("RGB", (W, H), CARTA)
    d = ImageDraw.Draw(tela)
    x, larg = 90, W - 180
    d.line([(x, 150), (x + 76, 150)], fill=BORLOTTO, width=5)
    d.text((x, 174), occhiello.upper(), font=bold(20), fill=BORLOTTO)
    for dim in (62, 54, 47, 41):
        f = bold(dim); righe = a_capo(d, titolo, f, larg)
        if len(righe) <= 3: break
    righe_corpo = a_capo(d, corpo, tondo_f(30), larg)
    alt_blocco = (200 if cifra else 0) + len(righe) * int(dim * 1.18) + 40 + len(righe_corpo) * 46
    y = 260 + max(0, (H - 420 - alt_blocco)) // 2          # centrato fra occhiello e piede
    if cifra:
        d.text((x, y), cifra, font=bold(150), fill=BORLOTTO); y += 200
    for r in righe:
        d.text((x, y), r, font=f, fill=INCHIOSTRO); y += int(dim * 1.18)
    y += 40
    for r in righe_corpo:
        d.text((x, y), r, font=tondo_f(30), fill=SOFT); y += 46
    piede(d, x, larg, H - 112)
    os.makedirs(FUORI, exist_ok=True)
    p = "%s/%s.jpg" % (FUORI, nome)
    tela.save(p, quality=90, optimize=True)
    return p


# ------------------------------------------------------------ scheda fagiolo
def scheda(slug, nome_f, numero, ruolo, motto, nome):
    tela = Image.new("RGB", (W, H), CARTA_SCURA)
    d = ImageDraw.Draw(tela)
    dim = 640
    r = Image.open("assets/img/ritratti/%s.jpg" % slug).convert("RGB")
    tela.paste(riempi(r, dim, dim), ((W - dim) // 2, 190))
    d.rectangle([(W - dim) // 2, 190, (W + dim) // 2, 190 + dim], outline=BORDO, width=4)
    x, larg = 90, W - 180
    d.text((W // 2, 120), "GUARDIANO N° %s" % numero, font=bold(22), fill=BORLOTTO, anchor="ma")
    d.text((W // 2, 890), nome_f, font=bold(62), fill=INCHIOSTRO, anchor="ma")
    d.text((W // 2, 972), ruolo, font=cors(30), fill=SOFT, anchor="ma")
    y = 1046
    for rg in a_capo(d, "«%s»" % motto, cors(27), larg)[:2]:
        d.text((W // 2, y), rg, font=cors(27), fill=INCHIOSTRO, anchor="ma"); y += 38
    piede(d, x, larg, H - 112)
    os.makedirs(FUORI, exist_ok=True)
    p = "%s/%s.jpg" % (FUORI, nome)
    tela.save(p, quality=90, optimize=True)
    return p


def apertura():
    fatti = []
    # ordine di pubblicazione: 1 per primo. Nella griglia il 9 finisce in alto a sinistra.
    fatti.append(manifesto("Cronaca ufficiale", "Dieci fagioli sono stati graziati.",
        "Domenica 8 novembre 2026, ore 11:15. Estratti dal sacchetto prima dell’ammollo, "
        "senza alcun merito, e deposti su un tovagliolo umido.", "01-la-grazia"))
    fatti.append(con_foto("assets/img/conclave-11-15.jpg", "Ore 11:15",
        "Il protocollo", "02-protocollo",
        "Campionamento stocastico ad alta precisione: due scosse e una mano dentro il sacchetto."))
    fatti.append(manifesto("In memoria", "Né la grazia né la cena.",
        "Dodici ore dopo, mentre il cuoco dormiva, gli altri 390 grammi non hanno avuto "
        "il destino di un normale fagiolo, che si chiama cena.", "03-390-grammi", cifra="390 g"))
    fatti.append(scheda("bud", "Bud", "01", "Il Leader",
        "L’acqua arriva. L’acqua arriva sempre.", "04-bud"))
    fatti.append(scheda("mary-poppins", "Meri Poppins", "09", "La Precisa",
        "Quattro millimetri. Non tre, non cinque.", "05-meri-poppins"))
    fatti.append(scheda("ugo-fantocci", "Ugo Fantocci", "06", "Il Perseguitato",
        "Io me lo ricordo.", "06-ugo"))
    fatti.append(con_foto("assets/img/conclave.jpg", "Lunedì 9 novembre",
        "I Dieci, primo giorno", "07-lunedi",
        "Disposizione assunta alle 11:19 di domenica e rimasta invariata."))
    fatti.append(con_foto("assets/img/conclave-martedi.jpg", "Martedì 10 novembre",
        "I Dieci non si ricordano niente", "08-martedi",
        "Quattro file ordinate. Nessuno sa chi le abbia disposte."))
    fatti.append(con_foto("assets/img/conclave-mercoledi.jpg", "Mercoledì 11 novembre",
        "Adesso si vede chi sta al centro", "09-mercoledi",
        "Otto in cerchio, due dentro. Le distanze non sono più uguali."))
    return fatti


if __name__ == "__main__":
    c = sys.argv[1] if len(sys.argv) > 1 else ""
    if c == "tondo":
        print(tondo())
    elif c == "apertura":
        for p in apertura(): print(p)
    elif c == "giorno":
        foto, occhiello, titolo, nome = sys.argv[2:6]
        print(con_foto(foto, occhiello, titolo, nome))
    else:
        print(__doc__); raise SystemExit(1)
