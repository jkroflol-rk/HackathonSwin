from django import forms
from .models import VlanConfig
from .models import WifiConfig


class SerialConnectionForm(forms.Form):
    com_port = forms.CharField(label='Input', max_length=30)
    


class VlanForm(forms.ModelForm):
    class Meta:
        model = VlanConfig
        fields = "__all__"

class PartialAuthorForm(forms.ModelForm):
    class Meta:
        model = VlanConfig
        exclude = ['title']

class WifiForm(forms.ModelForm):
    class Meta:
        model = WifiConfig
        fields = "__all__"

class PartialAuthorForm(forms.ModelForm):
    class Meta:
        model = WifiConfig
        exclude = ['title']