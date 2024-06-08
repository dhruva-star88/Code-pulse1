from django.db import models
from patient_details.models import PatientData
from django.contrib.auth.models import User

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
    
class EditedDoctorToPatientData(models.Model):
    pid = models.ForeignKey(PatientData, on_delete=models.CASCADE, default="ABCD")
    diagnosis = models.CharField(max_length=80)
    medications = models.CharField(max_length=400)
    life_style_changes = models.CharField(max_length=100)
    possible_procedures = models.CharField(max_length=100)
    next_appointment = models.CharField(max_length=100)
    lab_tests = models.CharField(max_length=100)
    reason = models.CharField(max_length=400, default="None")
    editedby = models.CharField(max_length=50, default="Ram Prasadh")
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.diagnosis
