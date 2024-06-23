{% load static %}
{% block content %}
    <h2>Are you sure you want to delete "{{ student.account_user_fullname }}"?</h2>
    <form method="post">
        {% csrf_token %}
        <button type="submit">Confirm Delete</button>
        <a href="{% url 'myFirstApp:read-data-student' %}">Cancel</a>
    </form>
{% endblock %}
