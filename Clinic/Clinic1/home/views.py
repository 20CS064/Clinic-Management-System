
from ast import Not
from email import message
import imp
from lib2to3.pgen2.token import NAME
from unicodedata import name
from django.shortcuts import render, HttpResponse,redirect
from django.template import context
from django.http import HttpResponseForbidden
# from home import models
from django.contrib import messages
#from rest_framework import viewsets
from django.contrib.auth import authenticate, login, logout
#from rest_framework.response import Response
#from rest_framework.views import APIView
from home.models import Contact, Patient,DoctorPage


# Create your views here.

def home(request):
    return render(request, 'index.html')


def login_user(request):

 if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']
        user_type = request.POST['user_type']

        user = authenticate(username=username, password=password)

        # doctor is superuser and receptionist is normaluser

        if user is  None:
            login(request, user)
            if user_type == 'Doctor':
                allPatients = Patient.objects.all()
               #print(allPatients)
                context = {'patients':allPatients}
                return render(request, 'view_patient.html',context)
            elif user_type == 'Receptionist':
                return render(request, 'registration.html')
            else:
                return render(request, '')
        else:
            messages.error(request, "Bad Credentials")
            return redirect('login')



 return render (request, 'login.html')

def appointment(request):
    if request.method =="POST":
        Your_Name = request.POST['Your-Name']
        Your_Email = request.POST['Your-Email']
        Date  = request.POST['Date']
        Phone_Number  = request.POST['Phone-Number']
        Patient_ID = request.POST['Patient-ID']
    return render (request, 'OA.html')
     #else:
     # return render (request,'index.html')

def about(request):
    return render (request, 'aboutus.html')

def view_Patient(request):
    allPatients = Patient.objects.all()
    #print(allPatients)
    context = {'patients':allPatients}
    return render (request,'view_patient.html',context)

def patientDetails(request):

    context={}


    return render (request,'patient_info.html',context)

def register(request):
    
    if request.method == "POST":

        Name= request.POST['Name']
        PID= request.POST['PID']
        Age= request.POST['Age']
        DOB= request.POST['DOB']
        gender= request.POST['gender']
        PN= request.POST['PN']
        email= request.POST['email']
        Add= request.POST['Add']
       # Password=request.POST['Password']

        ins = Patient(Patient_ID = PID, Name=Name, Age=Age, DOB=DOB, gender=gender, Phone=PN, email=email, Address=Add )
        ins.save()
    #else:
    if request.user.is_staff:
            return render (request, 'registration.html')
           # return render(request,'Auth/registration.html')
    else:
            return HttpResponseForbidden('<h1> 403 Forbidden <br>You are not allowed to access this page.</h1>')
    


def search(request):
    query = request.GET['query']
    allPatients= Patient.objects.filter(Patient_ID__icontains = query)
    params={'allPatients':allPatients }
    return render(request,'search.html',params) 

def patient_info(request):
    return render(request,'patient_info.html')

def login_patient(request):
    if request.method == 'POST':
        PUsername = request.POST['PUsername']
        PPassword = request.POST['PPassword']

        user = authenticate(username=PUsername, password=PPassword)
    
        if user is None:
            login(request, user)
            return render(request,'patient_info.html')

        else:
            messages.error(request, "Bad Credentials")
            return redirect('home')
    
    return render (request, 'patient_login.html')




def doctorpage(request):
    if request.method == "POST":

        Pateint_ID= request.POST['PID']
        Select_Symptom= request.POST['Symptom']
        Other_Symptom= request.POST['OtherSymptom']
        Select_Disease= request.POST['Disease']
        Other_Disease= request.POST['OtherDisease']
       # Medicine_Prescription= request.POST['MedicinePrescription']
        Test_Reports= request.POST['Report']
        Next_Appoinment= request.POST['Appoinment']
        Payment_Charges = request.POST['Charges']

        ins = DoctorPage(PID = Pateint_ID, Select_Symptom= Select_Symptom, OtherSymptom=Other_Symptom, Disease=Select_Disease, OtherDisease=Other_Disease , Reports= Test_Reports, Appoinment=Next_Appoinment, Payment_Charges=Payment_Charges)
        ins.save()
    else:
      if request.user.is_staff:
            return render (request, 'forms.html')
      else:
            return HttpResponseForbidden('<h1> 403 Forbidden <br>You are not allowed to access this page.</h1>')

    
def contact_us(request):

    if request.method =="POST":

        name = request.POST['name']

        email = request.POST['email']

        phone  = request.POST['phone']

        desc = request.POST['desc']

        ins = Contact(name = name, email=email,phone=phone,desc= desc)
        ins.save()

    return render (request,'contact_us.html')
