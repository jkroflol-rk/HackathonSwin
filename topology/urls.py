from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('config', views.ViewListConfig.as_view(), name='config'),
    path('addconfig', views.CreateConfigCLI.as_view(), name='addconfig'),
    path('<int:pk>/configdetail', views.ConfigDetail.as_view(), name='configdetail'),
    path('<int:pk>/deleteconfig', views.DeleteConfig.as_view(), name='deleteconfig'),
    path('connect', views.connect_serial, name='connect_serial'),
    path('test', views.Vlan_input.as_view(), name="adsa"),
    path('', views.Topology.as_view(), name="topology"),
    path('book', views.Book.as_view(), name="book"),
    path('document', views.Document.as_view(), name="document")
]

