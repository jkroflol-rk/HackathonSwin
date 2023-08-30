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
from .forms import SerialConnectionForm
import serial
import time
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

def connectserial(input, request):
    # creating your serial object
    hostname = request.session.get('hostname')
    ser = serial.Serial(
        port='COM1',  # COM is on windows, linux is different
        baudrate=9600,  # many different baudrates are available
        parity='N',  # no idea
        stopbits=1,
        bytesize=8,
        timeout=0.1  # 8 seconds seems to be a good timeout, may need to be increased
    )
    if request.session['enable'] == "1":
        header = hostname + "# "
    elif request.session['enable'] == "2":
        header = hostname + "> "
    else:
        header = hostname + "(config)# "
    if (request.session.get('history') == None):
        request.session['history'] = ""

    request.session['history'] += str(input) + "\n" + header
    

    # open your serial object
    ser.isOpen()
    # in this case it returns str COM3
    print(ser.name)

    # create a loop
    command = input
    command = str.encode(command+'\r\n')
    ser.write(command)
    time.sleep(0.1)
    ser.inWaiting()
    output = ser.read(225)
    output = output.decode("utf-8","ignore")
    return header
        # serial_data = SwitchConfig(output=output) #output = Switch# enable
        # serial_data.save()
# Press the green button in the gutter to run the script.



# def connectSerial(input, output, request):
#     input = int(input)
#     finaloutput = input * input

#     if (request.session.get('history') == None and request.session.get('output') == None):
#         request.session['history'] = ""
#         request.session['output'] = ""

#     request.session['history'] += str(finaloutput) + "\n"
    
#     request.session['output'] += str(finaloutput)
#     return finaloutput
class counter(TemplateView):
    template_name = "counter.html"



def connect_serial(request):
    if request.method == 'POST':
        form = SerialConnectionForm(request.POST)
        if form.is_valid():
            if request.session.get('enable') != None:
                com_port = form.cleaned_data['com_port']
                if  request.session.get('hostname') == None:
                    request.session['hostname'] = "Switch"


                    
                if com_port.split()[0] == 'hostname':
                    request.session['hostname'] = com_port[9::]

                if com_port == "enable":
                    request.session['enable'] = "1"
                elif com_port == "exit":
                    request.session['enable'] = "2"
                elif com_port == "conf t" and request.session['enable'] == "1":
                    request.session['enable'] = "3"

                if com_port == 'enable':
                    history = connectserial(com_port, request)
                elif com_port == 'exit':
                    history = connectserial(com_port, request)
                elif com_port.split()[0] == 'hostname':
                    history = connectserial(com_port, request)
                elif com_port == 'conf t':
                    history = connectserial(com_port, request)
                else:
                    if request.session['enable'] == "1":
                        subheader = "# "
                    elif request.session['enable'] == "2":
                        subheader = "> "
                    else:
                        subheader = "(config)# "                    
                    request.session['history'] += "invalid command" + "\n" + request.session['hostname'] + subheader

            else:
                request.session['enable'] = "2"
            return redirect('connect_serial')  # Redirect to a success page
    else:

        form = SerialConnectionForm()
        if request.session.get('history') != None:
            history = request.session.get('history')
        else:
            request.session['history'] = "Switch>"
            history = "Switch>"

    return render(request, 'connectionform.html', {'form': form, 'history': history})
    
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

class Book(TemplateView):
    template_name = 'switchbook.html'

class Document(TemplateView):
    template_name = 'document.html'