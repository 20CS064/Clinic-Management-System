from django.contrib import admin
from home.models import Contact, Patient,Doctor, city,receptionist,loginPatient ,DoctorPage,Appointment
from home.views import appointment
# Register your models here.

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(receptionist)
admin.site.register(DoctorPage)
admin.site.register(loginPatient)
admin.site.register(Appointment)
admin.site.register(Contact)
#admin.site.register(station)
admin.site.register(city)