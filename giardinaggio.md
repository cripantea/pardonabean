---
layout: page
title: Consigli di giardinaggio
permalink: /giardinaggio/
kicker: Rubrica di consigli non richiesti
description: "Consigli pratici per la germinazione domestica dei legumi, redatti dal Custode del Tovagliolo. Nessuno li ha chiesti. Sono tutti veri e sono tutti arrivati tardi."
---

Questa rubrica raccoglie i consigli pratici del Custode del Tovagliolo in materia di
germinazione domestica.

Va detto subito, perché è la cosa che li qualifica: **nessuno li ha chiesti**. Non esiste una
domanda a cui rispondano, non esiste un lettore che abbia scritto per sapere se il divano sia un
luogo di sorveglianza, e il Custode non ha titoli di studio in agronomia né in altro.

Va detto anche il resto. I consigli di questa pagina non sono inventati per fare ridere. Sono
ovvi, sono elementari, e ciascuno di quelli numerati con una data a piè di voce è stato appreso
in un momento preciso, di cui esiste il verbale. Un consiglio che arriva dopo il fatto non è un
consiglio: è un rendiconto scritto all'imperativo.

<div class="callout callout-warning">
  <p>
    <strong>Avvertenza sul valore di questi consigli.</strong> Tre di essi erano gi&agrave;
    noti al Custode prima dell&rsquo;8 novembre 2026, e li applicava. Li applicava, per la
    precisione, fino alle 21:50 di quella sera. Il registro pubblica la rubrica senza sostenere
    che leggerla serva: sostiene soltanto che esiste e che &egrave; gratis, due cose che
    distinguono questa pagina da altri rimedi comparsi di recente sul tovagliolo.
  </p>
</div>

{% assign consigli = site.data.consigli | sort: "numero" %}

<ol class="consigli">
  {%- for c in consigli %}
  <li class="consiglio" id="consiglio-{{ c.numero }}">
    <p class="consiglio-n">Consiglio n&deg; {{ c.numero }}</p>
    <h2 class="consiglio-titolo">{{ c.consiglio }}</h2>
    <p class="consiglio-testo">{{ c.testo | strip_newlines }}</p>
    {%- if c.appreso %}
    <p class="consiglio-appreso"><span>Appreso.</span> {{ c.appreso | strip_newlines }}</p>
    {%- endif %}
    {%- if c.nota %}
    <p class="consiglio-nota"><span>Nota del Custode.</span> {{ c.nota | strip_newlines }}</p>
    {%- endif %}
  </li>
  {%- endfor %}
</ol>

---

I consigli vengono aggiunti man mano che si imparano, il che significa man mano che qualcosa va
storto. Per i fatti da cui discendono: il [memoriale dei 390 grammi]({{ '/tragedia/' | relative_url }})
e il [Diario]({{ '/diario/' | relative_url }}).
