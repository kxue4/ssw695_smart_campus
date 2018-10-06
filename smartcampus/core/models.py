from django.db import models
from datetime import datetime


class Data(models.Model):
    id = models.IntegerField(primary_key=True)
    mac_address = models.CharField(max_length=100, null=True)
    datetime = models.DateTimeField(max_length=60, default=datetime.now)
    temperature = models.DecimalField(max_digits=10, decimal_places=2)
    humidity = models.DecimalField(max_digits=10, decimal_places=2)
    pressure = models.DecimalField(max_digits=10, decimal_places=2)
    air_quality = models.IntegerField()
    decibel = models.DecimalField(max_digits=10, decimal_places=4)


class Location(models.Model):
    id = models.IntegerField(primary_key=True)
    location_name = models.CharField(max_length=220)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.location_name


class SensorType(models.Model):
    id = models.IntegerField(primary_key=True)
    sensor_type = models.CharField(max_length=220)  # e.g., Temperature sensor, humidity sensor, etc
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)


class SingleBoardComputerType(models.Model):
    id = models.IntegerField(primary_key=True)
    computer_type = models.CharField(max_length=220)  # e.g., Raspberry Pi, Arduino
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)


class SingleBoardComputer(models.Model):
    id = models.IntegerField(primary_key=True)
    single_board_computer_name = models.CharField(max_length=220)
    single_board_computer_type_id = models.ForeignKey(SingleBoardComputerType, on_delete=models.CASCADE)
    operating_system = models.CharField(max_length=220)  # e.g., MacOS, Linux
    address = models.CharField(max_length=220)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.single_board_computer_name


class Temperature(models.Model):
    id = models.IntegerField(primary_key=True)
    temperature_level = models.DecimalField(max_digits=10, decimal_places=2)
    datetime = models.DateTimeField(max_length=60, default=datetime.now)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.temperature_level


class Pressure(models.Model):
    id = models.IntegerField(primary_key=True)
    pressure_level = models.DecimalField(max_digits=10, decimal_places=2)
    datetime = models.DateTimeField(max_length=60, default=datetime.now)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.pressure_level


class Humidity(models.Model):
    id = models.IntegerField(primary_key=True)
    humidity_level = models.DecimalField(max_digits=10, decimal_places=2)
    datetime = models.DateTimeField(max_length=60, default=datetime.now)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.humidity_level


class Decibel(models.Model):
    id = models.IntegerField(primary_key=True)
    decibel_level = models.DecimalField(max_digits=10, decimal_places=2)
    datetime = models.DateTimeField(max_length=60, default=datetime.now)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.decibel_level


class AirQuality(models.Model):
    id = models.IntegerField(primary_key=True)
    air_quality_level = models.IntegerField()
    datetime = models.DateTimeField(max_length=60, default=datetime.now)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.air_quality_level


class CampusBuilding(models.Model):
    id = models.IntegerField(primary_key=True)
    building_name = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.building_name


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    ip_address = models.CharField(max_length=220)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.ip_address



