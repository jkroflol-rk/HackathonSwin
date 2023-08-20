from django.db import models


# Create your models here.
class SwitchConfig(models.Model):
    input_data = models.TextField()
    output = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
