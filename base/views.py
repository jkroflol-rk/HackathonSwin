from django.shortcuts import render
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Notes
from django.http import Http404
from django.http.response import HttpResponseRedirect
from django.views.generic import CreateView,DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.
