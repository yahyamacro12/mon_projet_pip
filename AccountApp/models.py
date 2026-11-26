import django
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class user(AbstractUser):
   pass

class doctor(user):
    phone=models.CharField(max_length=8)
    licence_number=models.CharField(max_length=6,unique=True)
    specialties = models.ManyToManyField(Specialty, related_name='doctors', blank=True,nullable=True)

class patient(user):
    phone=models.CharField(max_length=8)
    birth_date=models.DateField()
    national_id=models.CharField(max_length=8,unique=True)

class Speciality(models.Model):
    name = models.CharField(max_length=100)