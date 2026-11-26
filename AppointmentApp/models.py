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
    #status=models.CharField(max_length=10,choices=[status.PENDING,status.CONFIRMED,status.CANCELLED],default=status.PENDING)
    doctor=models.ForeignKey('AccountApp.doctor',on_delete=models.CASCADE,null=True,blank=True)
    patient=models.ForeignKey('AccountApp.patient',on_delete=models.CASCADE,null=True,blank=True)