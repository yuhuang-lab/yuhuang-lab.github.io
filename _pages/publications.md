---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}


## Major Peer-reviewed Conference and Journal Papers

{% assign sorted = site.publications | sort: 'date' %}

{% for post in sorted reversed %}
  {% include archive-single-pub.html %}
{% endfor %}

## Book Sections

{% assign sorted = site.book_secs | sort: 'date' %}

{% for post in sorted reversed %}
  {% include archive-single-pub.html %}
{% endfor %}

## Patents

{% assign sorted = site.patents | sort: 'date' %}

{% for post in sorted reversed %}
  {% include archive-single-pub.html %}
{% endfor %}

## Minor Lightly-Reviewed Posters, Extended Abstracts, and Workshop Papers

{% assign sorted = site.minor_pubs | sort: 'date' %}

{% for post in sorted reversed %}
  {% include archive-single-pub.html %}
{% endfor %}

## Invited Talks and Presentation

{% assign sorted = site.talks | sort: 'date' %}

{% for post in sorted reversed %}
  {% include archive-single-pub.html %}
{% endfor %}
