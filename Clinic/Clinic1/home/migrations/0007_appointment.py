# Generated by Django 4.0.3 on 2022-04-19 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_doctorpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Your_Name', models.CharField(max_length=100, verbose_name='Your Name')),
                ('Your_Email', models.EmailField(max_length=100, verbose_name='Your Email')),
                ('Date', models.DateTimeField(verbose_name='Date')),
                ('Phone_Number', models.CharField(max_length=10, verbose_name='Phone Number')),
                ('Patient_ID', models.CharField(max_length=100, verbose_name='Patient ID')),
            ],
        ),
    ]
