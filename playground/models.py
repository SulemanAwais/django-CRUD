from datetime import date
import datetime

from django.db.models import Model, CharField, EmailField, TextField, DateField

# Create your models here.


class User(Model):
    firstName: str = CharField(max_length=20)
    lastName: str = CharField(max_length=20)
    email: str = EmailField()
    password: str = TextField()


class Task(Model):
    title: str = CharField(max_length=200, null=False, blank=False)
    content: str = TextField()
    day: date = DateField(default=date.today())
