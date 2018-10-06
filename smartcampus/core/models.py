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
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)


class Pressure(models.Model):
    id = models.IntegerField(primary_key=True)
    pressure_value = models.DecimalField(max_digits=10, decimal_places=2)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)


class Humidity(models.Model):
    id = models.IntegerField(primary_key=True)
    humidity_level = models.DecimalField(max_digits=10, decimal_places=2)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)


class Decibel(models.Model):
    id = models.IntegerField(primary_key=True)
    decibel_level = models.DecimalField(max_digits=10, decimal_places=2)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)


class AirQuality(models.Model):
    id = models.IntegerField(primary_key=True)
    air_quality_level = models.IntegerField()
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)


class CampusBuilding(models.Model):
    id = models.IntegerField(primary_key=True)
    building_name = models.CharField(max_length=120)
    location_id = models.CharField(max_length=120)
