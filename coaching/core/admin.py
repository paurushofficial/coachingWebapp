from django.contrib import admin
from . models import student, subject

admin.site.register(subject)
admin.site.register(student)