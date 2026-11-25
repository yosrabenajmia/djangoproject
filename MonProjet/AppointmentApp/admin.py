from django.contrib import admin
from .models import Appointment

@admin.action(description='Confirmer les RDV',
              permissions=['change'])
def mark_as_confirmed(modeladmin, request, queryset):
    queryset.update(status='CONFIRMED')

@admin.action(description='Annuler les RDV',
              permissions=['change'])
def mark_as_cancelled(modeladmin, request, queryset):
    queryset.update(status='CANCELLED') 

@admin.register(Appointment)
class AppointmentAdminPerso(admin.ModelAdmin):
    list_display = (
        'id', 'reason', 'status',
        'duration_minutes', 'appointment_date',
        'doctor', 'patient',
    )
    fieldsets = (
        ('Appointment Information', {
            'fields': ('reason', 'status')
        }),
        ('Appointment Details', {
            'fields': ('duration_minutes',
                       'appointment_date', 'doctor', 'patient')
        }),
        ('Non Editable', {
            'fields': ('created_at', 'updated_at')
        }),
    )
    readonly_fields = ('created_at', 'updated_at')
    actions = [mark_as_confirmed, mark_as_cancelled]