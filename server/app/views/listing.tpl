{% extends "layout.tpl" %}
{% block body %}
<h1><a href="/">quickstart</a>{% if type %} / {{ type }} {% endif %}</h1>
{% if files %}
<ul class="files">
  {% for file in files %}
  <li><a href="/{{type }}/{{ file }}">{{ file }}</a></li>
  {% endfor %}
</ul>
{% endif %}
{% endblock %}