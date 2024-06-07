from django.db import models

GENDER = (
    ("male", "Male"),

    ("female", "Female")
)


class PatientData(models.Model):
    patient_id = models.CharField(max_length=10, primary_key=True, default="NULL")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=50, choices=GENDER)
    phone_number = models.IntegerField(max_length=10)
    email = models.EmailField()
    emergency_contact_num = models.IntegerField(max_length=10)
    govt_id = models.CharField(max_length=50)
    symptoms = models.TextField(max_length=400, default="NOTHING")

    def __str__(self):
        self.first_name

