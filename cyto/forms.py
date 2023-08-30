from django import forms
from .models import VlanConfig, WifiConfig
class VlanForm(forms.ModelForm):
    class Meta:
        model = VlanConfig
        fields = "__all__"
class WifiForm(forms.ModelForm):
    class Meta:
        model = WifiConfig
        fields = "__all__"