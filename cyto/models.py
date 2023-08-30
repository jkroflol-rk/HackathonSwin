
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SwitchConfig(models.Model):
    input_data = models.TextField()
    output = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

# class VlanConfig(models.Model):
#     vlan_name = models.TextField()
#     host = models.IntegerField()
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="vlanconfigs")

# class WifiConfig(models.Model):
#     wifi_num = models.IntegerField()
#     printer_num = models.IntegerField()
#     devices_num = models.IntegerField()
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wificonfigs")