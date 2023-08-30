from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from cyto import final
from django.template import loader
def index(request):
    networkDevice, portDevice, vlan = final.cyto_json()
    saveJsonFile(networkDevice, "networkdevice.json")
    saveJsonFile(portDevice, "portdevice.json")
    saveJsonFile(vlan, "vlan.json")
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
def images(request):
    img = open("/images/3650.png", "rb")
    response = FileResponse(img)
    return response
def saveJsonFile(json, filename):
    # open text file
    text_file = open("./static/js/"+filename, "w")
    # write string to file
    text_file.write(json)
    # close file
    text_file.close()
from django.shortcuts import render

# Create your views here.
