from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, RegexValidator
from django.core.exceptions import ValidationError
from django.utils import timezone


# Méthode 1 : fonction validator pour birth_date
def validate_past_date(value):
    if value >= timezone.localdate():
        raise ValidationError("La date de naissance doit être antérieure à la date du jour.")


class User(AbstractUser):
    pass


class Specialty(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Doctor(User):
    phone = models.CharField(
        max_length=8,
        validators=[RegexValidator(r'^\d{8}$', "Le téléphone doit contenir 8 chiffres.")]
    )
    license_number = models.CharField(
        max_length=6,
        unique=True,
        validators=[MinLengthValidator(6)]
    )
    specialties = models.ManyToManyField(Specialty, related_name='doctors', blank=True)

    def __str__(self):
        return f"Dr {self.first_name} {self.last_name}"


class Patient(User):
    phone = models.CharField(
        max_length=8,
        validators=[RegexValidator(r'^\d{8}$', "Le téléphone doit contenir 8 chiffres.")]
    )
    birth_date = models.DateField(validators=[validate_past_date])
    national_id = models.CharField(
        max_length=8,
        unique=True,
        validators=[RegexValidator(r'^\d{8}$', "Le CIN doit contenir exactement 8 chiffres.")]
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"