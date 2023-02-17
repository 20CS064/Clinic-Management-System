from turtle import home
from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from home import views

admin.site.site_header = "Manali Clinic"
admin.site.site_title = "Welcome to Admin's Dashboard"
admin.site.index_title = "Welcome to this Portal"



urlpatterns = [
    path('',views.home, name='home'),
    path('login',views.login_user, name='login'),
   path('appointment',views.appointment, name='appointment'),
   path('Patient',views.view_Patient, name='view_Patient'),
   path('about',views.about, name='about'),
   path('register',views.register, name='register'),
   path('search',views.search,name='search'),
   path('Patient-Login',views.login_patient,name='login_patient'),
   path('Patient-Info',views.patient_info,name='patient_info'),
   path('doctorpage',views.doctorpage,name='doctorpage'),
   path('contact',views.contact_us,name='contact')
   
]