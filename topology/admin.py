from django.contrib import admin

from . import models

class ConfigAdmin(admin.ModelAdmin):
    list_display = ('input_data', 'output', 'timestamp')

admin.site.register(models.SwitchConfig, ConfigAdmin)
