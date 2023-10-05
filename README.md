# Building apps quickly with Django

## setup env

    pipenv --python 3.12
    pipenv install --pre django==5.0a
    pipenv shell

## setup django

    django-admin startproject project .
    chmod +x manage.py
    ./manage.py startapp demo

## link app

project/settings.py
```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "demo.apps.DemoConfig",
]
```

## create models

models.py
```python
class Person(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    bio = models.TextField(blank=True, null=True)
```

admin.py
```python
from . import models

admin.site.register(models.Person)
```

## run migrate

    ./manage.py makemigrations
    ./manage.py migrate
    ./manage.py createsuperuser --email admin@admin.com --username admin

## run server

    ./manage.py runserver

## add view and forms

`demo/views.py`
```python
from django.views import generic
from django.urls import reverse_lazy
# Create your views here.
from .models import Person


class PersonList(generic.ListView):
    model = Person


class PersonCreate(generic.CreateView):
    model = Person
    fields = "__all__"
    success_url = reverse_lazy("demo:index")


class PersonDelete(generic.DeleteView)
    model = Person
    success_url = reverse_lazy("demo:index")
```

## templates

`demo/templates/base.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Demo</title>
    <link rel="stylesheet" href="https://unpkg.com/mustard-ui@latest/dist/css/mustard-ui.min.css">
</head>
<body>

{% block content %}
{% endblock %}

</body>
</html>
```

`demo/templates/person_list.html`
```html
{% block content %}
    <ul>
	{% for person in object_list %}
        <li>
            <a href="mailto:{{ person.email }}">{{ person.name }}</a>
        </li>
	{% endfor %}
    </ul>
{% endblock %}
```

## urls

project/urls.py
```python
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("demo.urls")),
]
```

demo/urls.py
```python
from django.urls import path

from . import views

app_name = "demo"
urlpatterns = [
    path("", views.PersonList.as_view(), name="index"),
    path("create/", views.PersonCreate.as_view(), name="person-create"),
    path("<int:pk>/delete", views.PersonDelete.as_view(), name="person-delete"),
]

```

## run server again

    ./manage.py runserver

## addming items

`demo/templates/demo/person_form.html`
```html
{% extends "base.html" %}
{% block content %}
<h3>Add new person</h3>
<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
</form>
{% endblock %}
```

## removing items

`demo/templates/demo/person_list.html`
```html
<a href="{% url 'demo:person-delete' person.pk %}">X</a>
```

