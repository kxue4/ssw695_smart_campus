from django.db import models


class Data(models.Model):
    id = models.IntegerField(primary_key=True)
    mac_address = models.CharField(max_length=100, null=True)
    datetime = models.DateTimeField(max_length=60)
    temperature = models.DecimalField(max_digits=10, decimal_places=2)
    humidity = models.DecimalField(max_digits=10, decimal_places=2)
    pressure = models.DecimalField(max_digits=10, decimal_places=2)
    air_quality = models.IntegerField()
    decibel = models.DecimalField(max_digits=10, decimal_places=4)


class Location(models.Model):
    id = models.IntegerField(primary_key=True)
    location_name = models.CharField(max_length=120)


class Temperature(models.Model):
    id = models.IntegerField(primary_key=True)
    temperature = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)




