from django.urls import path

from . import views

urlpatterns = [
    path("", views.cyto, name="cyto"),
]