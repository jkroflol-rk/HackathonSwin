from django.urls import path
from . import views

urlpatterns = [
    path('menu', views.HomeView.as_view()),
]

