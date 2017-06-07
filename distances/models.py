from django.db import models

class House(models.Model):
    price = models.CharField(max_length=200,null=True)
    address = models.CharField(max_length=200,null=True)
    link = models.CharField(max_length=200,null=True)
    image = models.CharField(max_length=200,null=True)
    meters_walk_to_ov = models.IntegerField(default=0,null=True)
    time_walk_to_ov = models.IntegerField(default=0,null=True)
    time_walk_to_dart = models.CharField(max_length=200,null=True)
    dart_station = models.CharField(max_length=200,null=True)
    dart_for_sorting = models.IntegerField(default=0,null=True)

# Create your models here.
