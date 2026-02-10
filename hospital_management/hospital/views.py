from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Doctor, Patient, Appointment 
from .forms import DoctorForm, PatientForm, AppointmentForm

def home(request):
    return render(request, 'hospital/home.html')

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'hospital/doctor_list.html', {'doctors': doctors})

def add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm()
    return render(request, 'hospital/add_doctor.html', {'form': form})

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'hospital/patient_list.html', {'patients': patients})

def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'hospital/add_patient.html', {'form': form})

def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'hospital/appointment_list.html', {'appointments': appointments})

def add_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'hospital/add_appointment.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'hospital/signup.html', {'form': form})


