from pipes import Template
from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.template import loader
from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView, TemplateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse

from cyto import final, school, star
import json

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

class input(TemplateView):
    template_name = 'form.html'

def process(request):
    department = int(request.POST['departments'])
    names = request.POST.getlist('name[]')
    vlans = request.POST.getlist('host[]')

    output_array = []

    for i in range(0, department):
        output = f"{names[i]} : {vlans[i]}"
        output_array.append(output)

    if 'array' not in request.session:
        request.session['array'] = []

    request.session['array'].extend(output_array)
    request.session.modified = True

    with open('./static/js/output.json', 'w') as json_file:
        json.dump(output_array, json_file)

    return redirect('/cyto')

def saveJsonFile(json, filename):
    # open text file
    text_file = open("./static/js/"+filename, "w")
    # write string to file
    text_file.write(json)
    # close file
    text_file.close()
    


