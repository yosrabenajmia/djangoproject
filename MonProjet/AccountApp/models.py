from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, MaxLengthValidator


class User(AbstractUser):
    # You can add common fields here later if needed
    pass


class Speciality(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profile')
    license_number = models.CharField(
        max_length=6,
        unique=True,
        validators=[MaxLengthValidator(6)]
    )
    phone = models.CharField(max_length=8)
    specialties = models.ManyToManyField(Speciality, related_name='doctors')
    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'

    def __str__(self):
        return f"Dr. {self.user.get_full_name() or self.user.username}"


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient_profile')
    national_id = models.CharField(
        max_length=8,
        unique=True,
        validators=[RegexValidator(r"^\d{8}$", message="La CIN doit contenir 8 chiffres.")]
    )
    phone = models.CharField(max_length=8)
    birth_date = models.DateField()
    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'

    def __str__(self):
        return self.user.get_full_name() or self.user.username