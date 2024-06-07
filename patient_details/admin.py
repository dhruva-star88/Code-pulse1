from django.contrib import admin
from .models import PatientData

class PatientDataAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', )


admin.site.register(PatientData)

