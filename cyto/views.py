from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from cyto import final, school, star
from django.template import loader
from .models import VlanConfig, WifiConfig
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

   
def saveJsonFile(json, filename):
    # open text file
    text_file = open("./static/js/"+filename, "w")
    # write string to file
    text_file.write(json)
    # close file
    text_file.close()


