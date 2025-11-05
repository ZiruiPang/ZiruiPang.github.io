---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

{% include_relative include/intro.md %}

{% include_relative include/pub.md %}

{% include_relative include/edu.md %}

{% include_relative include/inter.md %}

{% include_relative include/mus.md %}

<div style="width: 500px; margin: 2em auto; text-align: center;">
  <p style="font-weight: bold;">🌍 Visitor Map</p>
  <script type='text/javascript' id='mapmyvisitors'
          src='https://mapmyvisitors.com/map.js?cl=ffffff&w=500&t=tt&d=4BolBiu1Bhj-fFYOcUr7N2TCnPlf0mhukLwA9Bwxo4g'></script>
</div>



