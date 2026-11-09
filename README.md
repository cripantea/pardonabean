# Pardon a Bean

Sito statico (Jekyll nativo + GitHub Pages) che documenta la germinazione, il salvataggio e
la memoria dei dieci fagioli borlotti scampati alla pentola rossa.

Dominio di produzione: **https://pardonabean.it** (vedi `CNAME`).

## Struttura

```
_config.yml      configurazione Jekyll (kramdown, permalink /diario/:year/:month/:day/:title/)
CNAME            dominio personalizzato
_layouts/
  default.html   scheletro HTML5: head, header + nav, footer, segnaposto AdSense
  page.html      pagine statiche (titolo, occhiello, lead)
  post.html      articolo del diario + navigazione prev/next
_includes/
  data-it.html   formatta una data in italiano ({% include data-it.html date=post.date %})
_posts/          articoli del diario (nome file: AAAA-MM-GG-slug.md)
assets/css/      foglio di stile unico
assets/img/      immagini (conclave.jpg, disastro-pentola.jpg, foto dei fagioli)
index.html       home: hero, griglia dei dieci, ultimi 5 aggiornamenti
fagioli.md       /fagioli/   biografie dei Dieci Guardiani
tragedia.md      /tragedia/  memoriale dei 390 grammi
diario.md        /diario/    archivio completo per anno
```

## Pubblicazione

Push su `main`, poi in *Settings → Pages* selezionare il branch `main` (cartella `/`) e
impostare `pardonabean.it` come dominio personalizzato. Nessuna dipendenza esterna: il sito
usa solo plugin inclusi nel parser standard di GitHub Pages.

### DNS richiesto

| Tipo | Nome | Valore |
|------|------|--------|
| A | `@` | `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153` |
| CNAME | `www` | `<utente>.github.io` |

## Anteprima locale (facoltativa)

```bash
gem install jekyll --user-install
jekyll serve
```

## Immagini

Le due fotografie del 9 novembre 2026 sono già pubblicate nel primo post e nella pagina
della Tragedia:

- `assets/img/disastro-pentola.jpg` — la pentola rossa con il fondo carbonizzato, il sacchetto
  dei 390 grammi perduti e la bacinella dell'acqua di filtraggio
- `assets/img/conclave.jpg` — la pentola accanto allo scolapasta con i superstiti recuperati

**Manca ancora** la foto dei Dieci sul tovagliolo umido. Quando sarà disponibile, caricarla come
`assets/img/tovagliolo.jpg` e aggiungere una `<figure>` nel post di lancio.

Per i segnaposto dei prossimi articoli è disponibile la classe `.img-placeholder`:

```html
<figure>
  <div class="img-placeholder">Segnaposto &mdash; <code>/assets/img/nome.jpg</code></div>
  <figcaption>Didascalia.</figcaption>
</figure>
```

## Google AdSense

Lo snippet è già predisposto, commentato, nell'`<head>` di `_layouts/default.html`:
decommentarlo e sostituire `ca-pub-XXXXXXXXXXXXXXXX` con l'ID editore reale.
