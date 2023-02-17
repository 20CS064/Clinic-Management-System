import email
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import PasswordInput

User_type = (
    ("Doctor", "Doctor"),
    ("Receptionist", "Receptionist"),
    ("View Patient","View Patient"),
)

Gender = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other","Other"),
)

Blood_group = (
    ("A+","A+"),
    ("A-","A-"),
    ("B+","B+"),
    ("B-","B-"),
    ("AB+","AB+"),
    ("AB-","AB-"),
    ("O+","O+"),
    ("O-","O-"),
)



Select_a_Symptom = (
    
    ("Select a Symptom","Select a Symptom"),
    ("Fever","Fever"),
    ("Headache","Headache"),
    ("Weight","Weight"),    
    ("Dizziness","Dizziness"),
    ("Jaundice","Jaundice"),
    ("Chest pain","Chest pain"),
    ("Back pain","Back pain"),
    ("Anxiety","Anxiety"),
    ("Muscle weakness","Muscle weakness"),
    ("Shivering","Shivering"),
    ("High BP","High BP"),
    ("Other","Other"),
)


Select_a_Disease = (
    ("Select Disease Detected","Select Disease Detected"),
    ("Flu","Flu"),
    ("Chickenpox","Chickenpox"),
    ("Asthma","Asthma"),
    ("Diabetes","Diabetes"),
    ("Obesity","Obesity"),
    ("Tuberculosis","Tuberculosis"),
    ("Atack","Atack"),
    ("Cancer","Cancer"),
    ("Knot found","Knot found"),
    ("Polio","Polio"),
    ("Other","Other"),
)



# Create your models here.

class Patient(models.Model):
    Patient_ID = models.CharField(max_length=10)
    Name = models.CharField(max_length=40)
    Age = models.CharField(max_length=3)
    DOB = models.DateTimeField()
    gender = models.CharField(max_length=20 ,choices=Gender)
    BloodGroup = models.CharField(max_length=5 ,choices=Blood_group)
    Phone = models.CharField(max_length=10)
    email=models.EmailField()
    Address = models.CharField(max_length=200) 
    #Password=models.CharField(max_length=30)

    def __str__(self):
        return self.Patient_ID + "-" + self.Name

class Doctor(models.Model):
    Username = models.CharField(max_length=200)
    Password = models.CharField(max_length=32)
    type = models.CharField(max_length=10,default='doctor')

    def __str__(self):
        return self.Username

    def is_doctor(self):
        return self.type

class receptionist(models.Model):
    Username = models.CharField(max_length=200)
    Password = models.CharField(max_length=32)
    type = models.CharField(max_length=15,default='Receptionist')


    def __str__(self):
        return self.Username

    def is_receptionist(self):
        return self.type

class loginPatient(models.Model):
    Username = models.CharField(max_length=200)
    Password = models.CharField(max_length=32)

    def __str__(self):
        return self.Username



class DoctorPage(models.Model):
     Patient_ID=models.CharField(max_length=10)
     Select_Symptom=models.CharField(max_length=50,choices=Select_a_Symptom) 
     Other_Symptom=models.CharField(max_length=50)
     Select_Disease=models.CharField(max_length=50,choices=Select_a_Disease)
     Other_Disease=models.CharField(max_length=50)
     Medicine_Prescription=models.TextField()
     Test_Reports=models.CharField(max_length=30)
     Next_Appoinment=models.DateTimeField()
     Payment_Charges=models.CharField(max_length=40)

class Appointment(models.Model):
    Your_Name = models.CharField('Your Name', max_length=100)
    Your_Email = models.EmailField('Your Email', max_length=100)
    Date = models.DateTimeField('Date')
    Phone_Number = models.CharField('Phone Number', max_length=10)
    Patient_ID= models.CharField('Patient ID', max_length=100)

    def __str__(self):
        return self.Your_name


class Contact(models.Model):

    sno = models.AutoField(primary_key=True)

    name = models.CharField(max_length=255)

    email = models.CharField(max_length=100)

    phone = models.CharField(max_length=10)

    messages= models.TextField()


class city(models.model):
    city_name=models.CharField(max_length=30)

#class station(models.Model):
#    city =models.ForeignKey(on_delete=models.CASCADE)
 #   stationName= models.CharField(max_length=40)
    