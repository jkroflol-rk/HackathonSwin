from django.shortcuts import render
from typing import Any
from django.db.models.query import QuerySet
# from .form import MyForm
from .models import SwitchConfig
from django.http import Http404
from django.http.response import HttpResponseRedirect
from django.views.generic import CreateView,DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
# Create your views here.

class CreateConfigCLI(CreateView):
    model = SwitchConfig
    fields = ['input_data', 'output']
    success_url = 'config'
    template_name = 'addconfig.html'

class ViewListConfig(ListView):
    model = SwitchConfig
    context_object_name = "configs"
    template_name = "viewlistconfig.html"

class DeleteConfig(DeleteView):
    model = SwitchConfig
    template_name = "deleteconfig.html"
    success_url = "/topology/config"
class ConfigDetail(DetailView):
    model = SwitchConfig
    context_object_name = "config"
    template_name = "configdetail.html"
    # login_url = "/login"
from .forms import SerialConnectionForm
import time
def connectSerial(input, output):
    # creating your serial object
    a = int(input)
    b = a * a 
    # while True:
    #     fdsf
    serial_data = SwitchConfig(input_data = input, output=b) #output = Switch# enable
    serial_data.save()
    return b
# Press the green button in the gutter to run the script.

def connect_serial(request):
    if request.method == 'POST':
        form = SerialConnectionForm(request.POST)
        if form.is_valid():
            com_port = form.cleaned_data['com_port']
            baud_rate = form.cleaned_data['baud_rate']
            connectSerial(com_port, baud_rate)
            return redirect('config')  # Redirect to a success page
    else:
        form = SerialConnectionForm()

    return render(request, 'connectionform.html', {'form': form})
    
    


