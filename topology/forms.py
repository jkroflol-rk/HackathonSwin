from django import forms

class SerialConnectionForm(forms.Form):
    com_port = forms.CharField(label='Input', max_length=10)
    baud_rate = forms.IntegerField(label='Baud Rate', initial=9600)
    