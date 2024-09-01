from django.db import models
from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    User = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=200, null=False, blank=False)
    content = models.TextField()
    due_date = models.DateField(null=True, blank=True)

    class Status(models.TextChoices):
        NOT_STARTED = 'NS', _('Not Started')
        IN_PROGRESS = 'IP', _('In Progress')
        COMPLETED = 'C', _('Completed')

    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.NOT_STARTED,
    )

    def __str__(self):
        return self.title
