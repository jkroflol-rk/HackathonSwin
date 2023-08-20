from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('config', views.CreateConfigCLI.as_view()),
]

