from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.urls import reverse
import logging
from django.contrib.auth.decorators import login_required

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

def index(request):
    return render(request, "home.html")


def signin(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        passwd = request.POST.get('pass')
        logger.debug(f"Attempting login with username: {username}")

        user = authenticate(request, username=username, password=passwd)
        if user is not None:
            auth_login(request, user)
            logger.debug(f"Login successful for user: {username}")
            return render(request, "doc-profile.html")
        else:
            logger.debug(f"Login failed for user: {username}")
            return redirect(reverse('index'))  # Use URL name for redirection

    return render(request, "login.html")

# Configure logging
logger = logging.getLogger(__name__)

@login_required
def retrive_p_data(request):
    if request.method == "POST":
        pid = request.POST.get('pid')
        if pid:
            logger.debug(f"Received PID: {pid}")
        else:
            logger.debug("PID not received")
         
    return render(request, "doc-profile.html")
