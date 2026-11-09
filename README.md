# Pardon a Bean

Sito statico (Jekyll nativo + GitHub Pages) che documenta la germinazione, il salvataggio e
la memoria dei dieci fagioli borlotti scampati alla pentola rossa.

Dominio di produzione: **https://pardonabean.it** (vedi `CNAME`).

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

### Dominio e percorsi

Il sito è servito dalla radice del dominio personalizzato:

```yaml
url: "https://pardonabean.it"
baseurl: ""
```

Tutti i percorsi interni usano il filtro `relative_url`, perciò si adattano automaticamente
al `baseurl`: per servire il sito da una sottocartella (es. `cripantea.github.io/pardonabean/`)
basta impostare `baseurl: "/pardonabean"` e rimuovere il file `CNAME`, senza toccare i link.

Record DNS da configurare presso il registrar. **Attenzione:** i quattro indirizzi IPv4 sono
quattro record A separati, tutti con nome `@`, un solo IP per record. Non vanno inseriti come
elenco separato da virgole in un unico record.

| Tipo | Nome | Valore | TTL |
|------|------|--------|-----|
| A | `@` | `185.199.108.153` | 300 |
| A | `@` | `185.199.109.153` | 300 |
| A | `@` | `185.199.110.153` | 300 |
| A | `@` | `185.199.111.153` | 300 |
| CNAME | `www` | `cripantea.github.io` | 300 |

Facoltativi, per raggiungibilità IPv6 (anch'essi un record AAAA ciascuno, nome `@`):

| Tipo | Nome | Valore |
|------|------|--------|
| AAAA | `@` | `2606:50c0:8000::153` |
| AAAA | `@` | `2606:50c0:8001::153` |
| AAAA | `@` | `2606:50c0:8002::153` |
| AAAA | `@` | `2606:50c0:8003::153` |

Verifica della propagazione:

```bash
dig +short pardonabean.it
dig +short www.pardonabean.it
```

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
