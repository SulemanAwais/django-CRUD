# Generated by Django 5.0.1 on 2024-01-17 07:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EMS', '0009_registrationid_employee_registration_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='domain',
            field=models.CharField(max_length=30),
        ),
    ]
