---
layout: page
title: Diario di Germinazione
permalink: /diario/
kicker: Archivio completo
description: "Tutti i bollettini dal tovagliolo umido, in ordine cronologico inverso."
---

Ogni voce di questo archivio è un bollettino dal tovagliolo: livello di umidità, stato dei
dieci, tensioni interne e — prima o poi — la prima radichetta. L'ordine è cronologico inverso:
in cima c'è l'aggiornamento più recente.

<p><strong>{{ site.posts.size }}</strong> {% if site.posts.size == 1 %}voce{% else %}voci{% endif %} in archivio.</p>

{% assign anni = site.posts | group_by_exp: "post", "post.date | date: '%Y'" %}
{% for anno in anni %}

<p class="archive-year">Anno {{ anno.name }} &middot; {{ anno.items.size }} aggiornament{% if anno.items.size == 1 %}o{% else %}i{% endif %}</p>

<ul class="post-list">
  {% for post in anno.items %}
  <li>
    <a class="post-item" href="{{ post.url | relative_url }}">
      <span class="post-item-date">{% include data-it.html date=post.date %}</span>
      <span>
        <span class="post-item-title">{{ post.title }}</span>
        <span class="post-item-excerpt">{{ post.description | default: post.excerpt | strip_html | truncate: 190 }}</span>
      </span>
    </a>
  </li>
  {% endfor %}
</ul>

{% else %}

<p class="post-list-empty">Nessun aggiornamento pubblicato: il tovagliolo è ancora all'asciutto.</p>

{% endfor %}

---

Per sapere chi sono i protagonisti di questi bollettini, consultare
[l'albo dei Dieci Guardiani]({{ '/fagioli/' | relative_url }}).
