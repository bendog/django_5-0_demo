from django.urls import path

from . import views

app_name = "demo"
urlpatterns = [
    path("", views.PersonList.as_view(), name="index"),
    path("create/", views.PersonCreate.as_view(), name="person-create"),
    path("<int:pk>/delete", views.PersonDelete.as_view(), name="person-delete"),
]
