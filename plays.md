---
title: Plays
---

{% for analysis in site.analyses %}
- [{{ analysis.title }}]({{ analysis.url }})
{% endfor %}
