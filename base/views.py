from django.shortcuts import render
# from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
# from .models import Notes
from django.http import Http404
from django.http.response import HttpResponseRedirect
from django.views.generic import CreateView,DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

class HomeView(TemplateView):
    template_name = 'index.html'
    # extra_context = {'today': datetime.today()}



def SignIn(request):
    return render(request, 'templates/SignIn.html')
def SignUp(request):
    return render(request, 'templates/SignUp.html')