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
  data-it.html       formatta una data in italiano ({% include data-it.html date=post.date %})
  conclave-mappa.html  fotografia del conclave con i numeri cliccabili
  analytics.html     script delle statistiche, solo in produzione
_data/
  posta.yml        lettere e risposte della rubrica /posta/
  taccuini.yml     frasi raccolte dal pozzo di saggezza di ogni Guardiano
_guardiani/      una scheda per fagiolo -> /fagioli/<slug>/ (collection nativa;
                 qui vivono le biografie, non nell'indice)
tools/
  ritratti.py      rigenera i ritratti ritagliandoli dalla foto del conclave
_posts/          articoli del diario (nome file: AAAA-MM-GG-slug.md)
assets/css/      foglio di stile unico
assets/img/      immagini (conclave.jpg, disastro-pentola.jpg, foto dei fagioli)
index.html       home: hero, griglia dei dieci, ultimi 5 aggiornamenti
fagioli.md       /fagioli/   indice dell'albo: mappa, nota metodologica, schede
posta.html       /posta/     corrispondenza con i lettori (generata da _data/posta.yml)
tragedia.md      /tragedia/  memoriale dei 390 grammi
diario.md        /diario/    archivio completo per anno
```

## Aggiungere una lettera alla Posta

Si tocca solo `_data/posta.yml`: nessuna modifica a `posta.html`. Si accoda un elemento
alla voce `lettere` del Guardiano che deve rispondere.

```yaml
    - da: Nome del lettore          # anche "Lettera firmata"
      luogo: Citta'
      data: 2026-11-12              # resa in italiano dalla pagina
      oggetto: Titolo breve
      testo: >
        La lettera.
      risposta: >
        La risposta del Guardiano.
      nota: >                       # facoltativo, in corsivo a fine scheda
        Chiosa della redazione.
```

I contatori in cima alla pagina e l'indice dei Guardiani si ricalcolano da soli; il numero
in home page (`{{ posta_tot }}`) pure. L'ancora di ogni lettera e' `/posta/#<slug>-<n>`,
dove `n` e' la posizione della lettera dentro la sezione del Guardiano.

## Nomi

Ogni Guardiano ha due diciture. Il **codice di registro** (`registro`) e' solo archivio.
Il **nome d'uso** (`nome`) e' quello che si legge ovunque, e `detto` ne spiega il motivo
in una subordinata che inizia con "per via di". Il layout le compone nella formula
"Fagiolo n. 01, iscritto come esemplare A/1 - detto Bud, per via di...".

Due nomi sono stati deformati di proposito per non ricalcare un marchio registrato:
Fantozzi e' diventato **Ugo Fantocci** e Mary Poppins e' diventata **Meri Poppins**.
Lo slug di quest'ultima resta `mary-poppins` perche' l'URL /fagioli/mary-poppins/ e'
gia' pubblico: non va cambiato. Onofrio e' "Il Marchese" e non "Il Marchese del Grillo",
che e' un titolo di film.

## Schede dei Guardiani

La biografia di un Guardiano sta in un posto solo: `_guardiani/<slug>.md`.
`/fagioli/` ne e' l'indice e si genera da solo tramite `_includes/albo-schede.html`,
quindi aggiungere o togliere un Guardiano non richiede di toccare l'indice. Le
ancore storiche (`/fagioli/#bud`) restano valide: sono sulle schede dell'indice.

Ogni fagiolo ha una scheda in `_guardiani/<slug>.md`, pubblicata come
`/fagioli/<slug>/`: ritratto, scheda d'identita', biografia, Taccuino e posta.
Il corpo del file e' la biografia; tutto il resto sta nel front matter.

```yaml
---
layout: guardiano
numero: "01"          # usato per ordinare e per la navigazione prec/succ
nome: Bud
slug: bud             # deve combaciare con _data/posta.yml e _data/taccuini.yml
registro: A/1         # codice d'archivio: lettera/numero, salta J e K (A..I, L)
genere: f             # solo per Mata Hari e Meri Poppins: fa scrivere "detta"
detto: per via della stazza e di una calma che nessuno ha ancora visto esaurirsi
ruolo: Il Leader
posizione: Centro esatto del tovagliolo
segni: Macchia scura a forma di continente sul fianco sinistro
motto: L'acqua arriva. L'acqua arriva sempre.
---
```

### Il ritratto

`python3 tools/ritratti.py bud` ritaglia il fagiolo da
`assets/img/conclave-mappa.jpg`, lo scontorna dal tovagliolo e lo salva in
`assets/img/ritratti/<slug>.jpg`, con la stessa inquadratura per tutti. Senza
argomenti rigenera tutti e dieci. Le coordinate dei fagioli stanno in cima allo
script e sono le stesse di `_includes/conclave-mappa.html`.

Per sostituire un ritratto con una fotografia propria basta mettere il file in
`assets/img/ritratti/<slug>.jpg`: la scheda lo prende da li'. Conviene che sia
quadrato e su fondo chiaro, per restare in serie con gli altri.

### Una raccolta nel Taccuino

Si accoda una voce in `_data/taccuini.yml`, sotto lo slug del Guardiano:

```yaml
bud:
  - data: 2026-11-16
    frasi:
      - Prima frase.
      - Seconda frase, facoltativa.
    nota: Circostanze della raccolta, a cura del Custode. Facoltativo.
```

La pagina ordina le raccolte dalla piu' recente e regge anche con una sola voce.

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

## Statistiche di visita

L'impianto è già nel sito ma **disattivato**: finché `analytics.provider` in `_config.yml` è
vuoto, non viene caricato alcuno script. Gli script vengono inclusi solo nella build di
produzione, quindi le visite in locale con `jekyll serve` non vengono conteggiate.

**Fornitore scelto: GoatCounter**, perché è cookieless e non richiede banner di consenso.
Manca solo il codice, che richiede la registrazione (gratuita per siti non commerciali) su
<https://www.goatcounter.com>: scelto un nome, lo si incolla in `code` e le statistiche partono.

```yaml
analytics:
  provider: "goatcounter"
  code: "pardonabean"   # il nome scelto in registrazione
```

Finché `code` è vuoto non viene caricato alcuno script, anche se `provider` è impostato.

| provider | `code` da inserire | Cookie | Banner di consenso |
|----------|--------------------|--------|--------------------|
| `goatcounter` | il nome scelto in fase di registrazione | no | non richiesto |
| `plausible` | il dominio (`pardonabean.it`) | no | non richiesto |
| `umami` | il website id | no | non richiesto |
| `cloudflare` | il token del beacon | no | non richiesto |
| `google` | l'id di misurazione `G-XXXXXXXXXX` | **sì** | **richiesto** |

> **Nota legale.** Google Analytics 4 usa cookie e profilazione: richiede un banner di consenso
> preventivo e una privacy policy, e il Garante Privacy italiano si è espresso contro il suo
> utilizzo per il trasferimento dei dati verso gli Stati Uniti. Le alternative in tabella sono
> cookieless e non richiedono consenso. Quando il provider è cookieless, il footer mostra
> automaticamente la nota «Statistiche di visita anonime e senza cookie»; la nota si disattiva
> con `nota_privacy: false`.

GitHub Pages non fornisce log di accesso lato server, quindi un contatore lato client è l'unico
modo per avere questi dati.

## Adempimenti privacy

- `privacy.md` → `/privacy/` è l'informativa, collegata dal footer di ogni pagina.
  **Vanno compilati i segnaposto del titolare del trattamento** (nome e contatto): finché
  restano `[DA COMPILARE]` l'informativa è incompleta.
- Nessun cookie viene installato, quindi non serve alcun banner.
- **Il rischio vero non sono le statistiche, è AdSense**: nell'Area Economica Europea gli annunci
  Google richiedono una CMP certificata IAB TCF v2.2 che raccolga il consenso prima del
  caricamento. Il segnaposto in `_layouts/default.html` è inerte e commentato: non va attivato
  finché la CMP non è predisposta.

## Google AdSense

Lo snippet è già predisposto, commentato, nell'`<head>` di `_layouts/default.html`:
decommentarlo e sostituire `ca-pub-XXXXXXXXXXXXXXXX` con l'ID editore reale.

## Card social (anteprima dei link)

Ogni articolo del Diario ha la propria immagine di condivisione 1200x630, con
dentro la fotografia di quel giorno. Si genera cosi', la mattina, subito dopo
aver convertito la foto:

    python3 strumenti/og-card.py assets/img/<foto-del-giorno>.jpg \
      <slug-del-post> "<Titolo dell'articolo>" "<Data per esteso>"

Lo script stampa la riga `immagine: /assets/img/og/<slug>.jpg` da incollare nel
front matter del post, subito sotto `date:`. Le pagine che non hanno il campo
`immagine` usano `assets/img/og-copertina.jpg`.
