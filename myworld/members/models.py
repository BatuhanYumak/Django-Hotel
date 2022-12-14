from django.db import models

from django import forms

# Create your models here.

# Hier maak ik een database model aan met de naam informatie. 
class Informatie(models.Model):
    city_id = models.CharField(max_length=100)
    city_name = models.CharField(max_length=100)
    hotel_id = models.CharField(max_length=100)
    hotel_name = models.CharField(max_length=100)

    def __str__(self):
        return self.city_name

class RegistrationForm(models.Model) :
    username = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30, blank=True)
