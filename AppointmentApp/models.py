from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.utils import timezone


class Appointment(models.Model):

    class Status(models.TextChoices):
        PENDING = 'PENDING', 'En attente'
        CONFIRMED = 'CONFIRMED', 'Confirmé'
        CANCELLED = 'CANCELLED', 'Annulé'

    reason = models.TextField()
    prescription = models.FileField(
        upload_to='prescriptions/',
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])]
    )
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)
    duration_minutes = models.PositiveIntegerField(default=30)
    appointment_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    doctor = models.ForeignKey('AccountApp.Doctor', on_delete=models.CASCADE, related_name='appointments')
    patient = models.ForeignKey('AccountApp.Patient', on_delete=models.CASCADE, related_name='appointments')

    class Meta:
        ordering = ['appointment_date']
        constraints = [
            models.UniqueConstraint(fields=['doctor', 'appointment_date'],
                                    name='unique_doctor_appointment_date')
        ]

    def clean(self):
        super().clean()
        if not self.appointment_date:
            return
        # Vérifier seulement à la création ou si la date a changé
        changed = True
        if self.pk:
            old = Appointment.objects.filter(pk=self.pk).values_list('appointment_date', flat=True).first()
            changed = old != self.appointment_date
        if changed and self.appointment_date <= timezone.now():
            raise ValidationError({'appointment_date': "La date doit être postérieure à maintenant."})