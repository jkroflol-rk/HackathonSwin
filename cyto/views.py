from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.template import loader
from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import VlanForm, WifiForm
from .models import VlanConfig, WifiConfig
from cyto import final, school, star

def cyto(request):
    networkDevice, portDevice, vlan = final.cyto_json()
    saveJsonFile(networkDevice, "networkdevice.json")
    saveJsonFile(portDevice, "portdevice.json")
    saveJsonFile(vlan, "vlan.json")
    template = loader.get_template('cyto.html')
    return HttpResponse(template.render())
def school_cyto(request):
    networkDevice, portDevice, vlan = school.main()
    saveJsonFile(networkDevice, "networkdevice.json")
    saveJsonFile(portDevice, "portdevice.json")
    saveJsonFile(vlan, "vlan.json")
    template = loader.get_template('cyto.html')
    return HttpResponse(template.render())
def star_cyto(request):
    networkDevice, portDevice, vlan = star.main()
    saveJsonFile(networkDevice, "networkdevice.json")
    saveJsonFile(portDevice, "portdevice.json")
    saveJsonFile(vlan, "vlan.json")
    template = loader.get_template('cyto.html')
    return HttpResponse(template.render())

# class VlanCreateView(LoginRequiredMixin, CreateView):
#     model = VlanConfig
#     success_url = ''
#     form_class = VlanForm
#     login_url = "/signin"
#
#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.user = self.request.user
#         self.object.save()
#         return HttpResponseRedirect(self.get_success_url())
#
# class WifiCreateView(LoginRequiredMixin, CreateView):
#     model = WifiConfig
#     success_url = ''
#     form_class = WifiForm
#     login_url = "/signin"
#
#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.user = self.request.user
#         self.object.save()
#         return HttpResponseRedirect(self.get_success_url())

def WifiFormPost(request):
    if request.method == 'POST':
        form = VlanForm(request.POST)
        if form.is_valid():
            request.session['vlan_name'] = form.cleaned_data['vlan_name']
            request.session['host'] = form.cleaned_data['host']
    else:

        form = SerialConnectionForm()
        if request.session.get('history') != None:
            history = request.session.get('history')
        else:
            history = "Nothing"

    return render(request, 'connectionform.html', {'form': form, 'history': history})

def saveJsonFile(json, filename):
    # open text file
    text_file = open("./static/js/"+filename, "w")
    # write string to file
    text_file.write(json)
    # close file
    text_file.close()


