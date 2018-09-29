from django.db import models
from datetime import date

class Post(models.Model):
    date = models.CharField(max_length=30)
    temperature = models.CharField(max_length=30)
    humidity = models.CharField(max_length=30)
    pressure = models.CharField(max_length=30)
    air_quality = models.CharField(max_length=30)
    decibel = models.CharField(max_length=30)

