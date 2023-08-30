from django.contrib import admin

from . import models

class ConfigAdmin(admin.ModelAdmin):
    list_display = ('input_data', 'output', 'timestamp')

admin.site.register(models.SwitchConfig, ConfigAdmin)

class VlanAdmin(admin.ModelAdmin):
    list_display = ('vlan_name', 'host')

admin.site.register(models.VlanConfig, VlanAdmin)

class WifiAdmin(admin.ModelAdmin):
    list_display = ('wifi_num', 'printer_num', 'devices_num')

admin.site.register(models.WifiConfig, WifiAdmin)



