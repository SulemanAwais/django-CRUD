import enum
from django.db import models
from django.db.models import CharField, ForeignKey, EmailField, CASCADE, OneToOneField


# Create your models here.


class Domain(models.Model):
    domain: CharField(max_length=100)


class RegistrationID(models.Model):
    registration_id: str = CharField(max_length=50)


class Employee(models.Model):
    first_name: str = CharField(max_length=30, null=False, blank=False)
    last_name: str = CharField(max_length=30, null=False, blank=False)
    email: str = EmailField(max_length=30, null=False, blank=False, unique=True)
    password: str = CharField(max_length=30, null=False, blank=False)
    domain = ForeignKey(Domain, on_delete=CASCADE, related_name='domain', default=1)
    registration_id = OneToOneField(RegistrationID, on_delete=CASCADE, related_name='registrationID', default=1)

    class Meta:
        verbose_name = 'employee'
