from math import *
import jsonify
import json

class deviceObject:
    def __init__(self, id, label, layer):
        self.data = {
            "id": id,
            "label": label,
            "layer": layer
        }
        self.switchPorts = {}
        self.connected = 0



class portObject:
    def __init__(self,source, target, sourceLabel, targetLabel):
        self.data = {
            "id": source["id"] + "-" + target["id"],
            "source": source["id"],
            "target": target["id"]
        }
        self.style = {
            "sourceLabel": sourceLabel,
            "targetLabel": targetLabel
        }

class Vlan:
    def __init__(self, host, id, name, switch, switchport):
        self.host = host
        self.id = id
        self.name = name
        self.port = {"switch": switch, "switchport": switchport}

def definePort(source, numPort, typePort):
    counter=1
    octet=0
    for i in range(numPort):
        if (counter>24):
            octet+=1
            counter=1
        if (typePort=="Gi"):
            portLabel=typePort+"1/"+str(octet)+"/"+str(counter)
        else: 
            if (typePort=="fa"):
                portLabel= typePort+str(octet)+"/"+str(counter)
        counter+=1
        source.switchPorts[portLabel]=False




def defineDevice(num,type,array,port,layer):
    for i in range(num):
        add_device=deviceObject(type+" "+str(i),type+" "+str(i), layer)
        definePort(add_device,port, "fa")
        array.append(add_device)
        
        


def connect(source,target,portDevice):
    for portSource in list(source.switchPorts.keys()):
            if (source.switchPorts[portSource]==False):
                portTarget = list(target.switchPorts.keys())[0]
                if (target.switchPorts[portTarget]==False):
                    new_port=portObject(source.data,target.data,portSource,portTarget)
                    portDevice.append(new_port)
                    source.switchPorts[portSource]=True
                    source.connected +=1
                    target.switchPorts[portTarget]=True
                    target.connected +=1
                    break
                
def createPortObject(port_array, source_devices, target_devices):
    for target in target_devices:
        for source in source_devices:
            connect(source,target,port_array)

def get_input_json():
    file = open('./static/js/outputhome.json', 'r')
    devices = json.loads(file.read())
    return devices

def main():
    #data input
    data_input = get_input_json()
    pcNum= int(data_input["pcnum"])
    printerNum= int(data_input["printernum"])
    wifiNum=int(data_input["wifinum"])
    sum=pcNum+printerNum+wifiNum
    accSwt_num=ceil(sum/23)
    portDevice = []
    accessDevice=[]
    router=[]
    portDevice = []
    accessSwitch=[]

    
    defineDevice(pcNum,"vlan",accessDevice,3,"device")
    defineDevice(printerNum,"Printer",accessDevice,3,"device")
    defineDevice(wifiNum,"Wifi",accessDevice,3,"device")

    defineDevice(accSwt_num,"Switch",accessSwitch,24,"Access")
    vlan=[]
    #define Router port
    add_router=deviceObject("router","Router","router")
    router.append(add_router)
    definePort(router[0],2,"Gi")
    

    createPortObject(portDevice, router, accessSwitch)
    createPortObject(portDevice, accessSwitch, accessDevice)
    for i in range(len(accessDevice)):
        new_Vlan=Vlan(3,accessDevice[i].data["id"],accessDevice[i].data["label"],accessSwitch[0].data["id"],[])
        vlan.append(new_Vlan)
    networkDevice =  accessSwitch  + router
    networkDeviceJson = json.dumps([z.__dict__ for z in networkDevice])
    portDeviceJson = json.dumps([z.__dict__ for z in portDevice])
    vlanJson = json.dumps([z.__dict__ for z in vlan])
    return networkDeviceJson, portDeviceJson, vlanJson
    
    
main()



    