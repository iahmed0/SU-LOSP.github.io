---
title: Plays
layout: page
---

<div id="analyses">
  {% for analysis in site.analyses %}
  <article>
    <h2><a href="{{ analysis.url }}">{{ analysis.title }}</a></h2>
    {% if analysis.summary %}
    <summary>{{ analysis.summary }}</summary>
    {% endif %}
  </article>
  {% endfor %}
</div>
