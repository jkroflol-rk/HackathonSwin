from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('signin', views.LoginInterfaceView.as_view(), name="signin"),
    path('signup', views.SignupView.as_view(), name='signup'),
    path('logintrue', views.LoginCorrect.as_view(), name='logintrue'),
]

