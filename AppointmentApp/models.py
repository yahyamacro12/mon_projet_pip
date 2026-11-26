from django.db import models

# Create your models here.
class status(models.TextChoices):
    PENDING = 'Pending', 'Pending'
    CONFIRMED = 'Confirmed', 'Confirmed'
    CANCELLED = 'Cancelled', 'Cancelled'

class Appointment(models.Model):
    reason=models.TextField()
    duration_minutes=models.DurationField()
    appointment_date=models.DateTimeField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,choices=status.choices,default=status.PENDING)
        doctor = models.ForeignKey(
            'AccountApp.Doctor',
            on_delete=models.CASCADE,
            related_name='appointments',nullable=True
        )
            patient = models.ForeignKey(
                'AccountApp.Patient',
                on_delete=models.CASCADE,
                related_name='appointments',nullable=True
            )
    #status=models.CharField(max_length=10,choices=[status.PENDING,status.CONFIRMED,status.CANCELLED],default=status.PENDING)