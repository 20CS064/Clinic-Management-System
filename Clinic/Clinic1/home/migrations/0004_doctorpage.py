# Generated by Django 4.0.3 on 2022-04-12 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_gender_patient_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctorpage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Patient_ID', models.CharField(max_length=10)),
                ('Name', models.CharField(max_length=40)),
                ('Age', models.CharField(max_length=3)),
                ('DOB', models.DateTimeField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=20)),
                ('BloodGroup', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=5)),
                ('Phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('Address', models.CharField(max_length=200)),
            ],
        ),
    ]
