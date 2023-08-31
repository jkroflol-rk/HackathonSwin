from django.urls import path

from . import views

urlpatterns = [
    path("", views.cyto, name="cyto"),
    path("school/",views.school_cyto, name="school-cyto"),
    path("star/",views.star_cyto, name="star-cyto"),
    path("process", views.process, name="process"),
    path("input", views.input.as_view(), name="input"),
    path("processhome", views.process_home, name="process_home"),
    path("inputhome", views.inputhome.as_view(), name="inputhome"),
    path("processschool", views.process_school, name="process_school"),
    path("inputschool", views.inputschool.as_view(), name="inputschool"),
    path("choice", views.choice.as_view(), name="choice"),

]