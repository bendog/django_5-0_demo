from django.shortcuts import render

from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
from .models import Person


class PersonList(generic.ListView):
    model = Person


class PersonCreate(generic.CreateView):
    model = Person
    fields = "__all__"
    success_url = reverse_lazy("demo:index")


class PersonUpdate(generic.UpdateView):
    model = Person
    fields = ["name", "email", "bio"]
    success_url = reverse_lazy("demo:index")


class PersonDelete(generic.DeleteView):
    model = Person
    success_url = reverse_lazy("demo:index")
