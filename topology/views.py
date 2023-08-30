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
from .forms import VlanForm
from .forms import WifiForm
from .models import WifiConfig
from .models import VlanConfig
from django.views.generic import TemplateView
# Create your views here.

class CreateConfigCLI(CreateView):
    model = SwitchConfig
    fields = ['input_data', 'output']
    success_url = 'config'
    template_name = 'addconfig.html'

class Topology(TemplateView):
    template_name = 'topology.html'

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
import serial
import time
# def connectSerial(input, output):
#     # creating your serial object
#     ser = serial.Serial(
#         port='COM6',  # COM is on windows, linux is different
#         baudrate=9600,  # many different baudrates are available
#         parity='N',  # no idea
#         stopbits=1,
#         bytesize=8,
#         timeout=0.1  # 8 seconds seems to be a good timeout, may need to be increased
#     )

#     # open your serial object
#     ser.isOpen()
#     # in this case it returns str COM3
#     print(ser.name)
#     # first command (hitting enter)

#     # wait a sec
#     time.sleep(0.1)
#     ser.inWaiting()
#     # get the response from the switch
#     input_data = ser.read(225)  # (how many bytes to limit to read)
#     input_data = input_data.decode("utf-8", "ignore")
#     # print response
#     print(input_data)
#     # create a loop
#     while 1:
#         command = input('')
#         command = str.encode(command+'\r\n')
#         ser.write(command)
#         time.sleep(0.1)
#         ser.inWaiting()
#         output = ser.read(225)
#         output = output.decode("utf-8","ignore")
#         print(output)
#         # serial_data = SwitchConfig(output=output) #output = Switch# enable
#         # serial_data.save()
def connectSerial(input, output, request):
    input = int(input)
    finaloutput = input * input

    if request.session.get('history') == None:
        request.session['history'] = ""
    request.session['history'] += str(finaloutput) + "\n"
    
    request.session['output'] += (finaloutput)
    return finaloutput



def connect_serial(request):
    if request.method == 'POST':
        form = SerialConnectionForm(request.POST)
        if form.is_valid():
            com_port = form.cleaned_data['com_port']
            baud_rate = form.cleaned_data['baud_rate']
            finaloutput =  connectSerial(com_port, baud_rate, request)
            return redirect('connect_serial')  # Redirect to a success page
    else:

        form = SerialConnectionForm()
        if(request.session.get('output') != None and request.session.get('history') != None):
            finaloutput = request.session.get('output')
            history = request.session.get('history')
        else:
            finaloutput = "Nothing"
            history = "Nothing"

    return render(request, 'connectionform.html', {'form': form, 'finaloutput': finaloutput, 'history': history})
    
class Vlan_input(CreateView):
    model = VlanConfig
    fields = ['vlan_name', 'host']
    success_url = 'config'
    template_name = 'addconfig.html'

class Wifi_input(CreateView):
    model = WifiConfig
    fields = ['wifi_num', 'printer_num', 'devices_num']
    success_url = 'config'
    template_name = 'addconfig.html'