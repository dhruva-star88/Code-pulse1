from django import forms

GENDER = (
    ("male", "Male"),

    ("female", "Female")
)

class PatientForm(forms.Form):
    patient_id = forms.CharField(max_length=10, primary_key=True, default="NULL")
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    dob = forms.DateField()
    gender = forms.CharField(max_length=50, choices=GENDER)
    phone_number = forms.IntegerField(max_length=10)
    email = forms.EmailField()
    emergency_contact_num = forms.IntegerField(max_length=10)
    govt_id = forms.CharField(max_length=50)
    symptoms = forms.CharField(max_length=400, default="NOTHING")