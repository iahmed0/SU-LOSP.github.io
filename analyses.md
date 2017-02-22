---
title: Plays
layout: page
---

<div id="analyses">
  {% for analysis in site.analyses %}
  <a class="play" href="{{ analysis.url }}">
    <h2>{{ analysis.title }}</h2>
    {% if analysis.year %}
    <h6>{{ analysis.year }}</h6>
    {% endif %}
    {% if analysis.summary %}
    <summary>{{ analysis.summary }}</summary>
    {% endif %}
  </a>
  {% endfor %}
</div>
