from django.contrib.auth.models import User
from django.db.models import Model, CharField, TextField, ForeignKey, SET_NULL


class Task(Model):
    User = ForeignKey(User, on_delete=SET_NULL, null=True, blank=True)
    title: str = CharField(max_length=200, null=False, blank=False)
    content: str = TextField()
    # day: date = DateField(default=date.today())
