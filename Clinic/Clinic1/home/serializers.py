from rest_framework import serializers
from .models import *

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ("PID", 'Name', 'Age', 'DOB', 'gender', 'bg', 'pn', 'Add' )
