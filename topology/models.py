from django.db import models


# Create your models here.
class SwitchConfig(models.Model):
    input_data = models.TextField()
    output = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class VlanConfig(models.Model):
    vlan_name = models.TextField()
    host = models.IntegerField()

class WifiConfig(models.Model):
    wifi_num = models.IntegerField()
    printer_num = models.IntegerField()
    devices_num = models.IntegerField()