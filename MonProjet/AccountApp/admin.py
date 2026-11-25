from django.contrib import admin
from .models import Doctor, Patient, Speciality,User

admin.site.register(User)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Speciality)
