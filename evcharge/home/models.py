from django.db import models

# Create your models here.

class stationdetails(models.Model):
    name = models.Charfield(max_length= 100)
    latitude = models.FloatField(max_length= 100)
    longitude = models.FloatField(max_length= 100)
    chargeprice = models.DecimalField(max_length=100)
    charger = models.CharField(max_length=50)