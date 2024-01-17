import enum
from django.db import models
from django.db.models import CharField, ForeignKey, EmailField, CASCADE, OneToOneField, IntegerField


# Create your models here.


class Domain(models.Model):
    domain_name = CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.domain_name

    class Meta:
        ordering = ['id']


class RegistrationID(models.Model):
    registration_id: str = CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.registration_id


class Employee(models.Model):
    first_name: str = CharField(max_length=30, null=False, blank=False)
    last_name: str = CharField(max_length=30, null=False, blank=False)
    email: str = EmailField(max_length=30, null=False, blank=False, unique=True)
    password: str = CharField(max_length=30, null=False, blank=False)
    employee_domain = ForeignKey(Domain, on_delete=models.CASCADE, related_name='domain', default=1)
    registration_id = OneToOneField(RegistrationID, on_delete=CASCADE, related_name='registrationID', default=1)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name = 'employee'
