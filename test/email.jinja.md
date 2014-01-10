# {{ subject.title() }} from {{ from }}

Sent to:
{% for recipient in [to] + cc %}
* {{ recipient }}
{% endfor %}

Body:
> {{ body }}
