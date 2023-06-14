from django.contrib import admin
from .models import Student, AdmissionResult

models_list = [Student, AdmissionResult]
admin.site.register(models_list)

