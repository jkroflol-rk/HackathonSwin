# Online Python compiler (interpreter) to run Python online.
from math import *


class deviceObject:
    def __init__(self, id, label, layer):
        self.data = {
            "id": id,
            "label": label,
            "layer": layer
        }
        self.switchPorts = {}
        self.connected = 0

class Room:
    def __init__(self, devices, id, name, switch, switchport):
        self.devices = devices
        self.id = id
        self.name = name
        self.port = {"switch": switch, "switchport": switchport}
        
        
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
        
def sortRoom(room):
    for x in range(0, len(room) - 1):
        for y in range(x + 1, len(room)):
            if room[x].devices > room[y].devices:
                room_tg = room[x]
                room[x] = room[y]
                room[y] = room_tg
    return room


def split_room(room):
    i = 0
    # Split vlan which has big value host
    while i < len(room):
        if room[i].devices > 23:
            numSplit = ceil(room[i].devices/23 )
            newHost = 24 - len(room) - numSplit + 1
            for j in range(numSplit - 1):
                newRoom = Room(23, room[i].id + "_" + str(j), room[i].name,"",[])
                room.append(newRoom)
            newRoom = Room(
                room[i].devices - 23 * (numSplit - 1),
                room[i].id + "_" + str(numSplit - 1),
                room[i].name,
                "",
                []
                )    
            room.append(newRoom)
            room.pop(i)
        else:
            i = i + 1
    return room


# Merge vlan which has small value host
def mergeRoom(room):
    i = 0
    while i < len(room) - 1:
        if (room[i].devices + room[i + 1].devices < 23):
            newRoom = Room(
                room[i].devices + room[i + 1].devices,
                room[i].id + "+" + room[i + 1].id,
                room[i].name,
                "",
                [],
            )
            room.append(newRoom)
            room.pop(i)
            room.pop(i)
            sortRoom(room)
        else:
            i = i + 1
    return room





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




def defineDevice(num,type,array,port):
    for i in range(num):
        add_device=deviceObject(type+str(i),type+" "+str(i), "device")
        definePort(add_device,port, "fa")
        array.append(add_device)
        

def connect(source,target,portDevice):
    for portSource in list(source.switchPorts.keys()):
            if (source.switchPorts[portSource]==False):
                portTarget = list(target.switchPorts.keys())[list(source.switchPorts.keys()).index(portSource)]
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

def connectRoom(vlan, accessDevice):
    for VLAN in vlan:
        portIndex = 0
        check = False
        for access in accessDevice:
            if access.connected == 1:
                for i in range(VLAN.devices):
                    for port in access.switchPorts:
                        if access.switchPorts[port] == False:
                            VLAN.port["switch"] = access.data["id"]
                            portIndex += 1
                            VLAN.port["switchport"].append(portIndex)
                            access.switchPorts[port] = True
                            access.connected += 1
                            break
                check = True
            if check == True:
                break

# Define port connect Access Switch to Vlan
def defineRoomPort(room, accessDevice, portDevice, number):
    for ROOM in room:
        labelTarget = ""
        startPort = ""
        endPort = ""
        for access in accessDevice:
            if ROOM.port["switch"] == access.data["id"]:
                startPort = list(access.switchPorts.keys())[number]
                endPort = list(access.switchPorts.keys())[number + ROOM.devices - 1]
                if endPort.find("fa") != -1:
                    labelTarget = startPort + "-" + endPort[4:]
                if endPort.find("Gi") != -1:
                    labelTarget = startPort + "-" + endPort[6:]
                new_port = portObject(
                    access.data, {"id": ROOM.id}, labelTarget, "Ethernet"
                )
                portDevice.append(new_port)

def main():
    #data input
    studentNum=1200
    room1=Room(40,"room1","Room 1","",[])
    room2=Room(50,"room2","Room 2","",[])
    room3=Room(35,"room3","Room 3","",[])
    
    
    room=[room1,room2,room3]
    room=split_room(room)
    room=sortRoom(room)
    room=mergeRoom(room)

    APs_num=ceil(studentNum/800)
    accSwt_num=2+len(room)
    
    portDevice = []
    accessDevice=[]
    router=[]
    
    accessSwitch=[]

    
    defineDevice(APs_num,"APs",accessDevice,8)
    defineDevice(accSwt_num,"accessSwt",accessSwitch,24)

    #define Router port
    add_router=deviceObject("router","Router","router")
    router.append(add_router)
    definePort(router[0],2,"Gi")
    
    connect(router[0],accessSwitch[0],portDevice)
    connect(accessSwitch[0],accessSwitch[1],portDevice)
    for i in range(len(accessDevice)):
        connect(accessSwitch[0],accessDevice[i],portDevice)
    for i in range(2,len(accessSwitch)):
        connect (accessSwitch[1],accessSwitch[i],portDevice)
        


    
    connectRoom(room,accessSwitch)
        
    defineRoomPort(room,accessSwitch,portDevice,1)   
    networkDevice =  room + accessDevice + accessSwitch  + router
    return networkDevice, portDevice
    
main()

