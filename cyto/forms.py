from django import forms
from .models import VlanConfig, WifiConfig
class VlanForm(forms.ModelForm):
    class Meta:
        model = VlanConfig
        fields = ('vlan_name', 'host')
        widgets = {
            'vlan_name': forms.TextInput(attrs={'class': 'form-control my-5 d-flex flex-column'}),
            'host': forms.TextInput(attrs={'class': 'form-control my-5 d-flex flex-column'})
        }
        labels = {
            'vlan_name: Department name'
            'host': 'Input the number of hosts'
        }
class WifiForm(forms.ModelForm):
    class Meta:
        model = WifiConfig
        fields = ('vlan_name', 'host')

    widgets = {
        'wifi_num': forms.TextInput(attrs={'class': 'form-control my-5 d-flex flex-column'}),
        'printer_num': forms.TextInput(attrs={'class': 'form-control my-5 d-flex flex-column'}),
        'devices_num': forms.TextInput(attrs={'class': 'form-control my-5 d-flex flex-column'})
    }
    labels = {
        'wifi_num': 'Input the amount of access point',
        'printer_num': 'Input the amount of printer',
        'devices_num': 'Input the amount of devices'
    }