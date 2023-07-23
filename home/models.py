# models.py
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField(null=True, blank=True)
    image = models.ImageField()

class Product(models.Model):
    pass

class Car(models.Model):
    car_name = models.CharField(max_length=100)
    speed = models.IntegerField(default=100)
#    read method
    def __str__(self) ->str:
        return self.car_name
    