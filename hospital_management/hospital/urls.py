from django.urls import path 
from . import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('' , views.home , name= 'home'),
    path('doctors/', views.doctor_list, name= 'doctor_list'),
    path('doctors/add/', views.add_doctor, name= 'add_doctor'),
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/add/', views.add_patient, name='add_patient'),
    
    path('login/', auth_views.LoginView.as_view(template_name='hospital/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointments/add/', views.add_appointment, name='add_appointment'),


]