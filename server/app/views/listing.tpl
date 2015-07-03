<!doctype html>
<html lang="en" dir="ltr">
    <head>
    <title>quickstart {% if type %} / {{ type }} {% endif %}</title>
    <meta name="description" content="">
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0">
    <link rel="stylesheet" href="/static/main.css">
    </head>
    <body>
    <h1><a href="/">quickstart</a>{% if type %} / {{ type }} {% endif %}</h1>
    {% if description %}
        <p>{{ description }}</p>
    {% endif %}
    {% if files %}
    <ul class="files">
        {% for file in files %}
            <li><a href="/{{type }}/{{ file }}">{{ file }}</a></li>
        {% endfor %}
    </ul>
    {% endif %}
    </body>
</html>
