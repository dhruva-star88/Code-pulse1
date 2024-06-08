from django import forms

class DoctorToPatientForm(forms.Form):
    diagnosis = forms.CharField(max_length=80)
    medications = forms.CharField(max_length=400)
    life_style_changes = forms.CharField(max_length=100)
    possible_procedures = forms.CharField(max_length=100)
    next_appointment = forms.CharField(max_length=100)
    lab_tests = forms.CharField(max_length=100)