# Generated by Django 5.0.1 on 2024-01-17 07:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EMS', '0004_alter_employee_domain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='domain',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='domain', to='EMS.domain'),
        ),
    ]
