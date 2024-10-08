# Generated by Django 5.0.8 on 2024-09-01 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0004_delete_user_task_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('NS', 'Not Started'), ('IP', 'In Progress'), ('C', 'Completed')], default='NS', max_length=2),
        ),
    ]
