from django.db import models


class Airquality(models.Model):
    id = models.IntegerField(primary_key=True)
    air_quality_level = models.IntegerField()
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    datetime = models.DateTimeField()

    class Meta:
        db_table = 'core_airquality'


class Campusbuilding(models.Model):
    id = models.IntegerField(primary_key=True)
    building_name = models.CharField(max_length=120)
    created_at = models.DateTimeField()
    location = models.ForeignKey('Location', on_delete=models.CASCADE)

    class Meta:
        db_table = 'core_campusbuilding'


class Decibel(models.Model):
    id = models.IntegerField(primary_key=True)
    decibel_level = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    datetime = models.DateTimeField()

    class Meta:
        db_table = 'core_decibel'


class Humidity(models.Model):
    id = models.IntegerField(primary_key=True)
    humidity_level = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    datetime = models.DateTimeField()

    class Meta:
        db_table = 'core_humidity'


class Location(models.Model):
    id = models.IntegerField(primary_key=True)
    location_name = models.CharField(max_length=220)
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()

    class Meta:
        db_table = 'core_location'


class Pressure(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    pressure_level = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    datetime = models.DateTimeField()

    class Meta:
        db_table = 'core_pressure'


class Sensortype(models.Model):
    id = models.IntegerField(primary_key=True)
    sensor_type = models.CharField(max_length=220)
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()

    class Meta:
        db_table = 'core_sensortype'


class Singleboardcomputer(models.Model):
    id = models.IntegerField(primary_key=True)
    single_board_computer_name = models.CharField(max_length=220)
    operating_system = models.CharField(max_length=220)
    address = models.CharField(max_length=220)
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    single_board_computer_type_id = models.ForeignKey('Singleboardcomputertype', on_delete=models.CASCADE)

    class Meta:
        db_table = 'core_singleboardcomputer'


class Singleboardcomputertype(models.Model):
    id = models.IntegerField(primary_key=True)
    computer_type = models.CharField(max_length=220)
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()

    class Meta:
        db_table = 'core_singleboardcomputertype'


class Temperature(models.Model):
    id = models.IntegerField(primary_key=True)
    temperature_level = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    datetime = models.DateTimeField()

    class Meta:
        db_table = 'core_temperature'


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    ip_address = models.CharField(max_length=220)
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'core_user'


class Data(models.Model):
    # id = models.IntegerField(primary_key=True)
    mac = models.CharField(max_length=17, blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    pres = models.FloatField(blank=True, null=True)
    hum = models.FloatField(blank=True, null=True)
    gas = models.FloatField(blank=True, null=True)
    lux = models.IntegerField(blank=True, null=True)
    db = models.FloatField(blank=True, null=True)
    dt = models.DateTimeField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'data'


class Feedback(models.Model):
    name = models.CharField(max_length=220, null=True)
    email = models.EmailField(max_length=70, null=True)
    feedback = models.CharField(max_length=220, null=True)
