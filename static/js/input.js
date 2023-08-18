class configGenerate {
    constructor(device, config) {
        this.device = device;
        this.config = config;
    }
}
var deviceConfig = [];
deviceIp = 2;
vlanIp = 2;
function GenerateConfigInput(swtDevice, portDevice, vlanDevice) {
    command_line = "";
    swtDevice.forEach(element => {
        var hostname = element.data.id;
        command_line = "hostname " + hostname + "\n!\n";
        command_line += "no ip domain-lookup \n!\n";
        if (element.data.id.includes("Swt") == true) {
            command_line += "ip default-gateway 192.168.1.1\n!\n"
            command_line += "interface vlan1\n";
            command_line += "ip address 192.168.1." + deviceIp + " 255.255.255.0\nno shut\n!\n";
            deviceIp++;
        }

        vlanDevice.forEach(elementvlan => {
            if (hostname.includes("Swt") == true) {
                var vlan_name = elementvlan.name;
                command_line += elementvlan.id + "\n";
                command_line += "name " + vlan_name + " \n!\n";
            }
        });
        if (hostname.includes("router") == true) {
            command_line += "interface g0/0/1\n" + "encapsulation dot1q 1\n" + "ip address 192.168.1.1 255.255.255.0\n" + "no shut" + "\n!\n";
            vlanDevice.forEach(vlanElement => {
                command_line += "interface g0/0/1." + vlanElement.id.substring(5, vlanElement.id.length) + "\n";
                command_line += "encapsulation dot1q " + vlanElement.id.substring(5, vlanElement.id.length) + "\n";
                command_line += "ip address 192.168." + vlanIp + ".1" + " 255.255.255.0\n";
                vlanIp++;
                command_line += "exit\n!\n";
            });
        }
        if (hostname.includes("Swt") == true) {
            portDevice.forEach(portElement => {
                if ((portElement.data.source == hostname) && (portElement.data.target.includes("vlan") == false)) {
                    command_line += "interface range " + portElement.style.sourceLabel + "\n";
                    command_line += "switchport mode trunk \n!\n";
                } else if ((portElement.data.source == hostname) && (portElement.data.target.includes("vlan") == true)) {
                    command_line += "interface range " + portElement.style.sourceLabel + "\n";
                    var switchport = "access ";
                    command_line += "switchport mode " + switchport + "\n";
                    command_line += "switchport access " + portElement.data.target + "\n!\n";
                }
                if ((portElement.data.source.includes("router") == true) && (hostname.includes("core") == true)) {
                    command_line += "interface range " + portElement.style.sourceLabel + "\n";
                    command_line += "switchport mode trunk \n!\n";
                }
            });
        }
        deviceConfig.push(new configGenerate(hostname, command_line));
        command_line = "";
    });
    return deviceConfig;
}
command_router = GenerateConfigInput(router, portDevice, vlan);
command_coreSwt = GenerateConfigInput(coreDevice, portDevice, vlan);
command_distSwt = GenerateConfigInput(distDevice, portDevice, vlan);
command_access = GenerateConfigInput(accessDevice, portDevice, vlan);
var box = document.body.querySelector('.collapse');
console.log(box);
deviceConfig.forEach(command_config => {
    var button = document.createElement('button');
    button.innerText = command_config.device;
    button.classList.add('collapsible');
    box.appendChild(button);
    var txt_command = document.createElement('div');
    txt_command.innerText = command_config.config;
    txt_command.classList.add('content');
    box.appendChild(txt_command);
});

console.log(deviceConfig);