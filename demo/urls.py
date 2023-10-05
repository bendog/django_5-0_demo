from django.urls import path

from . import views

app_name = "demo"
urlpatterns = [
    path("", views.PersonList.as_view(), name="index"),
    path("create/", views.PersonCreate.as_view(), name="person-create"),
    path("<int:pk>/update", views.PersonUpdate.as_view(), name="person-update"),
    path("<int:pk>/delete", views.PersonDelete.as_view(), name="person-delete"),
]
