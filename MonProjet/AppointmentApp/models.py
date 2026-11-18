from django.db import models

class Status(models.TextChoices):
        PENDING = "PENDING", "En attente"
        CONFIRMED = "CONFIRMED", "Confirmé"
        CANCELLED = "CANCELLED", "Annulé"

class Appointment(models.Model):
    reason = models.TextField() #1
    appointment_date = models.DateTimeField()
    duration_minutes = models.PositiveIntegerField(default=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    status = models.CharField(
        max_length=9, choices=Status.choices,
        default=Status.PENDING
    )

    prescription = models.FileField( #2
        upload_to="prescriptions/", blank=True
    )
    doctor = models.ForeignKey(
        "AccountApp.Doctor", on_delete=models.CASCADE
    )
    patient = models.ForeignKey(
        "AccountApp.Patient", on_delete=models.CASCADE
    )

