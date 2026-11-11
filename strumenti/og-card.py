#!/usr/bin/env python3
"""Compone la card social 1200x630 di un articolo: fotografia del giorno a
destra, titolo e data a sinistra, nei colori del sito.

    python3 strumenti/og-card.py <foto.jpg> <slug> "<titolo>" "<data estesa>"

Salva in assets/img/og/<slug>.jpg e stampa il percorso da mettere nel front
matter del post, nel campo "immagine:".
"""
import sys, os
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
CARTA, INCHIOSTRO, SOFT, BORLOTTO, BORDO = "#faf8f5", "#23251f", "#4a4d44", "#9e3b3b", "#ded8cc"
FONT = "/System/Library/Fonts/Supplemental/"


def g(nome, dim):
    return ImageFont.truetype(FONT + nome, dim)


def a_capo(testo, font, larghezza, disegno):
    righe, riga = [], ""
    for parola in testo.split():
        prova = (riga + " " + parola).strip()
        if disegno.textlength(prova, font=font) <= larghezza:
            riga = prova
        else:
            righe.append(riga)
            riga = parola
    if riga:
        righe.append(riga)
    return righe


def componi(foto_path, slug, titolo, data_estesa):
    tela = Image.new("RGB", (W, H), CARTA)
    d = ImageDraw.Draw(tela)

    # fotografia del giorno: ritaglio quadrato centrato sul piattino
    foto = Image.open(foto_path).convert("RGB")
    lato = min(foto.size)
    sx = (foto.width - lato) // 2
    sy = max(0, (foto.height - lato) // 2)
    foto = foto.crop((sx, sy, sx + lato, sy + lato)).resize((H, H), Image.LANCZOS)
    tela.paste(foto, (W - H, 0))
    d.line([(W - H, 0), (W - H, H)], fill=BORDO, width=3)

    x = 64
    larg = W - H - 128

    d.line([(x, 70), (x + 72, 70)], fill=BORLOTTO, width=4)
    d.text((x, 92), "DIARIO DI GERMINAZIONE", font=g("Georgia Bold.ttf", 18), fill=BORLOTTO)

    # il titolo si adatta: meno righe servono, piu' grande viene
    for dim in (54, 48, 42, 37, 33):
        f = g("Georgia Bold.ttf", dim)
        righe = a_capo(titolo, f, larg, d)
        if len(righe) <= 4:
            break
    y = 150
    for riga in righe:
        d.text((x, y), riga, font=f, fill=INCHIOSTRO)
        y += int(dim * 1.22)

    d.text((x, y + 26), data_estesa, font=g("Georgia Italic.ttf", 24), fill=SOFT)

    d.line([(x, H - 104), (x + larg, H - 104)], fill=BORDO, width=2)
    d.text((x, H - 78), "pardonabean.it", font=g("Georgia Bold.ttf", 25), fill=INCHIOSTRO)
    d.text((x + larg, H - 76), "Anno I della Grazia", font=g("Georgia Italic.ttf", 21),
           fill=SOFT, anchor="ra")

    os.makedirs("assets/img/og", exist_ok=True)
    fuori = "assets/img/og/%s.jpg" % slug
    tela.save(fuori, quality=90, optimize=True)
    return fuori


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(__doc__)
        raise SystemExit(1)
    print("immagine: /" + componi(*sys.argv[1:]))
