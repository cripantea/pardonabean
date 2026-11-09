# Pardon a Bean

Sito statico (Jekyll nativo + GitHub Pages) che documenta la germinazione, il salvataggio e
la memoria dei dieci fagioli borlotti scampati alla pentola rossa.

Indirizzo attuale: **https://cripantea.github.io/pardonabean/**
Dominio previsto: `pardonabean.it` (non ancora registrato).

## Struttura

```
_config.yml      configurazione Jekyll (kramdown, permalink, url + baseurl)
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

Push su `main`, poi in *Settings → Pages* selezionare il branch `main` e la cartella `/ (root)`.
Nessuna dipendenza esterna: il sito usa solo quanto incluso nel parser standard di GitHub Pages.

### Configurazione attuale: sito di progetto su github.io

Il sito è servito da una sottocartella, quindi `_config.yml` imposta:

```yaml
url: "https://cripantea.github.io"
baseurl: "/pardonabean"
```

Tutti i percorsi interni usano il filtro `relative_url`, perciò si adattano automaticamente
al `baseurl`: non ci sono URL assoluti scritti a mano da correggere.

### Passaggio al dominio pardonabean.it

Quando il dominio sarà registrato:

1. in `_config.yml` → `url: "https://pardonabean.it"` e `baseurl: ""`
2. ricreare il file CNAME → `echo pardonabean.it > CNAME`
3. in *Settings → Pages* impostare il dominio personalizzato e, a certificato emesso,
   attivare *Enforce HTTPS*

Record DNS da configurare presso il registrar:

| Tipo | Nome | Valore |
|------|------|--------|
| A | `@` | `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153` |
| CNAME | `www` | `cripantea.github.io` |

> Il file `CNAME` va tenuto fuori dal repo finché il dominio non risolve: la sua sola presenza
> fa sì che GitHub Pages reindirizzi l'URL github.io al dominio personalizzato, rendendo il
> sito irraggiungibile.

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
- `assets/img/conclave.jpg` — i Dieci sul tovagliolo umido, ore 23:48 (formato verticale:
  la `<figure>` usa la classe `.figure-ritratto`, che ne limita la larghezza a 440px)

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
