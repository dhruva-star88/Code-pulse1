
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.urls import reverse
import logging
from django.contrib.auth.decorators import login_required
from patient_details.models import PatientData
from django.contrib.auth.models import User
from .forms import DoctorToPatientForm
from .models import DoctorToPatientData, EditedDoctorToPatientData

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

def index(request):
    return render(request, "home.html")

@login_required
def signin(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        request.session["username"] = username
        passwd = request.POST.get('pass')
        logger.debug(f"Attempting login with username: {username}")

        user = authenticate(request, username=username, password=passwd)
        if user is not None:
            auth_login(request, user)
            logger.debug(f"Login successful for user: {username}")
            user = User.objects.get()
            user_data = {
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                }   
            return render(request, "doc-profile.html", user_data)
    
        else:
            logger.debug(f"Login failed for user: {username}")
            return redirect('index')  # Use URL name for redirection

    return render(request, "login.html")



# Configure logging
logger = logging.getLogger(__name__)
@login_required
def retrive_p_data(request):
    logger.debug("Entering retrive_p_data view")
    print(request.method == "POST")
    if request.method == "POST":
        pid = request.POST.get('pid')
        logger.debug(f"Received PID: {pid}")
        if pid:
            request.session["pid"] = pid
            logger.debug(f"Processing PID: {pid}")
            # Add logic to handle the PID and retrieve data
        else:
            logger.debug("PID not received")
    else:
        logger.debug("Not a POST request")
    return render(request, "doc-profile.html")

def pat_report(request):
    # pid = request.session.get("pid")
    pid = "EFGH"
    patient_data = PatientData.objects.get(patient_id=pid)
    logger.debug(f"Patient Data: {patient_data.gender}")
    pat_name = patient_data.first_name
    gender = patient_data.gender
    age = patient_data.Age
    symptoms = patient_data.symptoms
    context={
        'name': pat_name,
        'gen': gender,
        'age': age,
        'symp': symptoms
    }

    return render(request, "pat_details.html", context)


def doc_to_pat_report(request):
    if request.method == "POST":
        diagnosis = request.POST.get('radioOption')
        medications = request.POST.get('textbox')
        life_style_changes = request.POST.getlist('checkbox')
        possible_procedures = request.POST.get('dropdown1')
        next_appointment = request.POST.get('dropdown2')
        lab_tests = request.POST.get('dropdown3')

        DoctorToPatientData.objects.create(diagnosis=diagnosis, medications=medications, life_style_changes=life_style_changes,
                                           possible_procedures=possible_procedures, next_appointment=next_appointment, lab_tests=lab_tests)
 

    return render(request, "doc_to_pat_report.html")


def pat_prev_rec(request):
    return render(request, "pat-prev-record.html")

def edit_record(request):
    if request.method == "POST":
        diagnosis = request.POST.get('radioOption')
        medications = request.POST.get('textbox')
        life_style_changes = request.POST.getlist('checkbox')
        possible_procedures = request.POST.get('dropdown1')
        next_appointment = request.POST.get('dropdown2')
        lab_tests = request.POST.get('dropdown3')
        reason = request.POST.get('reason')
        

        EditedDoctorToPatientData.objects.create(diagnosis=diagnosis, medications=medications, life_style_changes=life_style_changes,
                                           possible_procedures=possible_procedures, next_appointment=next_appointment, lab_tests=lab_tests,
                                           reason=reason)

    return render(request, "edit-record.html")