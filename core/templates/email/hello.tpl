{% extends 'mail_templated/base.tpl' %}
{% block subject %}
Hello {{name}}
{% endblock %}
{% block html %}
This is a <strong>html</strong> message
{% endblock %}