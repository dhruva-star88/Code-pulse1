from django.db import models
from patient_details.models import PatientData

GENDER=(
    ('male', 'Male'),
    ('female', 'Female')
)

class DoctorToPatientData(models.Model):
    pid = models.ForeignKey(PatientData, on_delete=models.CASCADE, default="ABCD")
    diagnosis = models.CharField(max_length=80)
    medications = models.CharField(max_length=400)
    life_style_changes = models.CharField(max_length=100)
    possible_procedures = models.CharField(max_length=100)
    next_appointment = models.CharField(max_length=100)
    lab_tests = models.CharField(max_length=100)

    def __str__(self):
        return self.diagnosis
