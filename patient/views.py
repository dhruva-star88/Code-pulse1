from django.shortcuts import render
from patient_details.models import PatientData
from doctor.models import DoctorToPatientData

def pat_id_page(request):
    if request.method == "POST":
        pid = request.POST.get('pid')
        print(pid)
        

    return render(request, "pat_id_page.html")

def pat_hosp_record(request):
    pid = "ABCD"
    print(pid)
    patient_data = PatientData.objects.get(patient_id=pid)
    doctor_report = DoctorToPatientData.objects.get(pid=pid)
    context ={
    'pat_id' : patient_data.patient_id,
    "pat_fname" : patient_data.first_name,
    "pat_lname" : patient_data.last_name,
    "gender ": patient_data.gender,
    "age" : patient_data.Age,
    "email": patient_data.email,
    "ph_num" : patient_data.phone_number,
   " emg_num" : patient_data.emergency_contact_num,
   " govt_id ": patient_data.govt_id,
    "symptoms" : patient_data.symptoms,
    "dig" : doctor_report.diagnosis,
    "medic" : doctor_report.medications,
    "life_ch" : doctor_report.life_style_changes,
    "poss_pro ": doctor_report.possible_procedures,
   " next_app ": doctor_report.next_appointment,
   " lab_tests" :doctor_report.lab_tests
    }
    
    return render(request, "pat_record.html", context)
