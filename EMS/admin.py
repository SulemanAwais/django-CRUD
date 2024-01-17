from django.contrib import admin
from EMS.models import Employee, Domain, RegistrationID
# Register your models here.
admin.site.register(Employee)
admin.site.register(Domain)
admin.site.register(RegistrationID)