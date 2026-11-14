---
title: "Ripresa: passaggio di consegne a una nuova sessione"
---

PASSAGGIO DI CONSEGNE — aggiornato sabato 14 novembre 2026, dopo la pubblicazione
del sesto bollettino (commit 66d49c1, verificato live).

Questo file sta in _drafts/ e non viene mai pubblicato. Serve a una sessione nuova
che riprenda il lavoro senza avere la cronologia della chat precedente.
LA REGIA NARRATIVA VERA E' IN `_drafts/arco-bud-calendario.md`: leggerlo subito dopo
questo, e' piu' lungo e piu' importante.


=================================================================
1. CHE COS'E'
=================================================================
pardonabean.it — sito Jekyll nativo su GitHub Pages (nessun plugin fuori da quelli
standard di GitHub Pages). Repo locale: /Users/cristianpantea/progetti/pardonabean
Branch unico: main. Push su main = deploy.

Racconta, in italiano e in registro burocratico ironico-solenne, la vicenda di dieci
fagioli borlotti graziati la notte dell'8 novembre 2026, quando 390 grammi di borlotti
sono stati lasciati sul fuoco e bruciati in una pentola rossa. I dieci superstiti
germinano su un tovagliolo di carta e ogni mattina esce un bollettino.

La voce narrante e' "il Custode del Tovagliolo", che si autodefinisce "il registro".
Parla in terza persona, verbalizza, data e ora tutto, si astiene dalle conclusioni e
mette in fila i fatti lasciando che il lettore li congiunga.


=================================================================
2. REGOLE NON NEGOZIABILI
=================================================================
FISICA. I fagioli non si muovono da soli, non hanno arti, non scrivono (dettano: la
  redazione trascrive) e il piu' grande misura undici millimetri. Nessuna gag puo'
  violare questo. Il Custode non descrive MAI il meccanismo con cui la disposizione
  sul tovagliolo cambia: fotografa prima e dopo.

LA FOTO COMANDA. Ogni articolo parte dalla fotografia reale del giorno, mandata
  dall'autore. Lo stato di germinazione osservato ha la precedenza su qualunque
  snodo previsto dal calendario: se compare una radice, slitta tutto il resto.
  Mai inventare uno stato botanico che nella foto non si vede.

EPISTEMOLOGIA. Dal 10 novembre il Custode dichiara di non riuscire piu' ad attribuire
  un nome a ciascun esemplare. I rilievi sono quindi "di posizioni, non di individui".
  E' il pilastro che regge tutto il sito: non romperlo per comodita' di trama.

MOTIVO DI FONDO (dichiarato dall'autore): "viviamo in una societa' priva di memoria
  collettiva". Non va MAI enunciato come tesi dentro un pezzo. Si esprime solo in
  fatti e in procedura. Il sito non accusa nessuno di dimenticare: mostra quanto e'
  ragionevole, comodo e veloce farlo.

SATIRA. Si scrive la proposta, mai la risposta. Nessun decreto finto, nessuna firma
  di ministri, nessuna dichiarazione attribuita a persone reali, nessun atto ufficiale
  fabbricato. La satira sta sul prodotto e sulla procedura, mai sul venditore.

CONSIGLI DI GIARDINAGGIO (/giardinaggio/). Il consiglio e' inutile perche' e' OVVIO o
  perche' arriva TARDI. Mai perche' e' assurdo.


=================================================================
3. VINCOLI DI SICUREZZA E PRIVACY — ANCORA IN VIGORE
=================================================================
- ADSENSE NON VA ATTIVATO. Il segnaposto in _layouts/default.html resta commentato
  con l'avvertenza. Nell'AEE servirebbe una CMP certificata IAB TCF v2.2 prima del
  caricamento degli annunci. L'autore ha detto esplicitamente: "non voglio ricevere
  qualche multa per 10 fagioli".
- Statistiche: GoatCounter, cookieless, nessun banner. Resta cosi'.
- In privacy.md i segnaposto [NOME E COGNOME DA COMPILARE] e [INDIRIZZO E-MAIL DA
  COMPILARE] NON vanno riempiti senza via libera esplicita dell'autore.
- Nessuna raccolta di dati personali. Il meccanismo delle "firme" alla proposta vive
  solo nei commenti Instagram: niente moduli, niente piattaforme di petizioni.
- Instagram: non fare login, non creare account, non digitare password. La
  pubblicazione sul profilo la fa l'autore a mano.


=================================================================
4. STATO AL 14 NOVEMBRE 2026
=================================================================
Pubblicati sei bollettini in _posts/ (permalink /diario/AAAA/MM/GG/titolo/):
  09/11  La grande fuga dal lavandino
  10/11  I dieci non si ricordano niente
  11/11  Adesso si vede chi sta al centro
  12/11  Nessuno aveva accusato Bud
  13/11  Il centro non ha messo radice
  14/11  Nessuno si e' mosso di un millimetro      <- ultimo

Pagine: / (home) · /fagioli/ (albo + 10 schede) · /posta/ · /diario/ · /giardinaggio/
        · /tragedia/ (il memoriale, con il processo alla pentola e la proposta di
        legge) · /privacy/

Numerazione dei giorni: giorno N = data - 8 novembre 2026. Il 14/11 e' il Giorno 6.
Il calcolo e' in Liquid, in index.html e in _includes/nav-giorni.html, con
  {%- assign zero = "2026-11-08" | date: "%s" | plus: 0 -%}

Stato botanico al 14/11: 10 su 10 presenti, 5 radichette (una biforcata), 5 senza,
disposizione identica a quella del 13/11 (prima notte senza spostamenti), due
sfumature giallo-verdi all'attacco col seme, zona asciutta sul lato destro.


=================================================================
5. STRUTTURA E COMANDI
=================================================================
_config.yml      collection "guardiani" -> /fagioli/:name/ ; permalink del diario
_data/           consigli.yml (10 voci) · posta.yml · proposta.yml · taccuini.yml
_includes/       data-it.html · nav-giorni.html · conclave-mappa.html · albo-schede.html
                 · analytics.html
_layouts/        default.html (head, nav, footer) · page.html · post.html
_drafts/         arco-bud-calendario.md (LA REGIA) · questo file. Mai pubblicati.
assets/img/      conclave-<giorno>.jpg (foto del giorno, 1080x1920)
                 og/<slug>.jpg (card social 1200x630)
social/          materiale Instagram, escluso dal build (404 sul sito live)
strumenti/       og-card.py · instagram.py

Build locale (il binario NON e' nel PATH):
  /Users/cristianpantea/.local/share/gem/ruby/4.0.0/bin/jekyll build --quiet

Card OG di un articolo:
  python3 strumenti/og-card.py assets/img/conclave-<giorno>.jpg <slug> "<Titolo>" "<Data estesa>"

Card Instagram del giorno:
  python3 strumenti/instagram.py giorno assets/img/conclave-<giorno>.jpg \
      "Giorno N — <giorno> <data>" "<Titolo>" <NN>-<giorno>
  (ultimo file prodotto: social/17-sabato.jpg)

Deploy e verifica (attendere SIA lo SHA SIA lo stato "built"):
  git push origin main
  gh api repos/:owner/:repo/pages/builds/latest --jq '"\(.commit) \(.status)"'
  curl -s -o /dev/null -w "%{http_code}\n" https://pardonabean.it/<percorso>/

Validazione YAML (python3 non ha pyyaml su questa macchina, ruby si'):
  ruby -ryaml -e 'YAML.safe_load(File.read("_data/taccuini.yml"), permitted_classes: [Date])'

TRAPPOLE NOTE:
 - NON usare sed per sostituire stringhe che contengono "&": nella replacement sed
   espande & col testo trovato. Usare python3.
 - Il CSS e' cache-bustato in _layouts/default.html con
   ?v={{ site.github.build_revision | default: site.time | date: '%s' | slice: -8, 8 }}
   Se l'autore manda uno screenshot "senza stile", e' cache del browser, non il sito.
 - jekyll serve staccato a volte non rigenera: lanciare jekyll build esplicito.
 - Ogni post vuole DUE immagini nel front matter: `immagine:` (card OG, col titolo
   gia' stampato sopra) e `foto:` (la fotografia nuda, usata in home). Senza `foto:`
   la home mostra il titolo due volte.


=================================================================
6. RITUALE DI PUBBLICAZIONE DEL BOLLETTINO QUOTIDIANO
=================================================================
L'autore manda la foto del giorno e scrive una riga tipo "ecco la foto di oggi".
Da li' in poi, senza chiedere altro:
  1. Confrontare la foto con quella del giorno prima (assets/img/conclave-*.jpg):
     contare radichette, tegumenti aperti, posizioni, umidita'. Il fatto nuovo esce
     dal confronto, non dalla fantasia.
  2. Salvare la foto come assets/img/conclave-<giorno>.jpg, 1080x1920, qualita' 88.
  3. Leggere _drafts/arco-bud-calendario.md e prendere i fili gia' carichi per quel
     giorno. Verificare che non contraddicano la foto.
  4. Scrivere _posts/AAAA-MM-GG-<slug>.md con front matter completo
     (layout, title, date con +0100, immagine, foto, tags, description).
     Struttura collaudata: Il conto / il fatto del giorno / le sezioni di trama /
     Stato della missione / "Quello che il registro e' tenuto ad aggiungere".
  5. Aggiungere le voci del giorno in _data/taccuini.yml, in testa alla lista del
     Guardiano (le voci di Patrocle hanno `direzione:` invece di `frasi:`).
  6. Generare card OG e card Instagram, e aggiungere la didascalia in
     social/didascalie.md.
  7. Aggiornare _drafts/arco-bud-calendario.md con un blocco "— FATTO" e con i fili
     che restano carichi per il giorno dopo.
  8. jekyll build, commit, push, attendere Pages, verificare in live.


=================================================================
7. FILI APERTI — I PROSSIMI GIORNI
=================================================================
Il dettaglio sta in arco-bud-calendario.md, in fondo. In sintesi:

DOMENICA 15
  - Onofrio sogna per la seconda notte lo stesso numero, 934. Toto' lo interpreta
    con la smorfia (90 = 'a paura, 34 = 'a capa) e dichiara il sogno MAL RIUSCITO.
    Il Custode annota che 90034, nella forma con lo zero, e' un CAP italiano
    esistente e che il registro si e' fermato li'. NON dire quale comune.
  - L'avvertenza del Custode sulle bustine esce come consiglio numerato in
    /giardinaggio/ (il n. 9 e' gia' li' dal 13 novembre e prepara il terreno).
  - La richiesta di parere n. 1 di Meri Poppins e' pendente presso la richiedente:
    terza promessa di atto scritto in tre giorni.
  - Sette giorni di stessa inquadratura: si puo' montare il time-lapse (Reel).

SETTIMANA DEL 16
  - Si scopre che il Custode e' originario di Corleone. NESSUNO deve pronunciare
    "Corleone" prima di allora. Il Custode non si schermisce e non aggiunge
    smentite: ne ha gia' fatta una non richiesta il 12 novembre.
  - Fine settimana: Michele in Florida.

CARTA MAI SPESA: l'undicesimo fagiolo, rimesso nel sacchetto.


=================================================================
8. IN SOSPESO, LATO AUTORE
=================================================================
 - Instagram @pardonabean: riordinare la bio, mettere social/profilo-tondo.jpg come
   immagine del profilo, seguire il profilo da cristi72095, poi caricare in ordine
   i post 01->09, 10-giovedi, 11-15 (carosello della Giornata dei 390), 16-venerdi,
   17-sabato. Le didascalie sono tutte in social/didascalie.md.
 - _data/proposta.yml, campo `consensi`: si aggiorna A MANO man mano che arrivano
   commenti su Instagram. Oggi e' 0.
 - DOMANDA ANCORA SENZA RISPOSTA, da riproporre una volta sola: la description di
   tragedia.md contiene l'espressione "olocausto culinario". E' pronta la
   sostituzione:
     "Cronistoria della notte in cui 390 grammi di fagioli borlotti sono stati
      lasciati sul fuoco e non hanno avuto ne' la grazia ne' la cena."
   Serve solo un si'.
