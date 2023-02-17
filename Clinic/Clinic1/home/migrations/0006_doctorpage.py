# Generated by Django 4.0.3 on 2022-04-15 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_loginpatient_delete_doctorpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctorpage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Patient_ID', models.CharField(max_length=10)),
                ('Select_Symptom', models.CharField(choices=[('Select a Symptom', 'Select a Symptom'), ('Fever', 'Fever'), ('Headache', 'Headache'), ('Weight', 'Weight'), ('Dizziness', 'Dizziness'), ('Jaundice', 'Jaundice'), ('Chest pain', 'Chest pain'), ('Back pain', 'Back pain'), ('Anxiety', 'Anxiety'), ('Muscle weakness', 'Muscle weakness'), ('Shivering', 'Shivering'), ('High BP', 'High BP'), ('Other', 'Other')], max_length=50)),
                ('Other_Symptom', models.CharField(max_length=50)),
                ('Select_Disease', models.CharField(choices=[('Select Disease Detected', 'Select Disease Detected'), ('Flu', 'Flu'), ('Chickenpox', 'Chickenpox'), ('Asthma', 'Asthma'), ('Diabetes', 'Diabetes'), ('Obesity', 'Obesity'), ('Tuberculosis', 'Tuberculosis'), ('Atack', 'Atack'), ('Cancer', 'Cancer'), ('Knot found', 'Knot found'), ('Polio', 'Polio'), ('Other', 'Other')], max_length=50)),
                ('Other_Disease', models.CharField(max_length=50)),
                ('Medicine_Prescription', models.TextField()),
                ('Test_Reports', models.CharField(max_length=30)),
                ('Next_Appoinment', models.DateTimeField()),
                ('Payment_Charges', models.CharField(max_length=40)),
            ],
        ),
    ]