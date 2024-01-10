from django.db.models import Model, CharField, EmailField, TextField

# Create your models here.


class User(Model):
    firstName: str = CharField(max_length=20)
    lastName: str = CharField(max_length=20)
    email: str = EmailField()
    password: str = TextField()