from django.contrib import admin
from .models import User, Client, Lawyer, Service, Appointment
# Register your models here.


admin.site.register([User, Client, Lawyer, Service, Appointment])

