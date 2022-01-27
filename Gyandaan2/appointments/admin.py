from django.contrib import admin

from . models import Appointment, Mentor, Schedule, Service, ServiceBooked, ServiceProvided, Student

# Register your models here.

admin.site.register(Student)
admin.site.register(Mentor)
admin.site.register(Schedule)
admin.site.register(Appointment)
admin.site.register(Service)
admin.site.register(ServiceBooked)
admin.site.register(ServiceProvided)
