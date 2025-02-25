{% for file in files %}
  {% if file|lower endswith ('.png', '.jpg', '.jpeg', '.gif', '.svg') %}
    ![{{ file }}]({{ file }})
  {% endif %}
{% endfor %}
