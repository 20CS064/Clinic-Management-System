# Generated by Django 4.0.3 on 2022-04-15 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_doctorpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='loginPatient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=200)),
                ('Password', models.CharField(max_length=32)),
            ],
        ),
        migrations.DeleteModel(
            name='doctorpage',
        ),
    ]