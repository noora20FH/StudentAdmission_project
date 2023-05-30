from django.contrib import admin

from .models import AdminApp  # add this


class AdmissionData(admin.ModelAdmin):  # add this
    list_display = ('name', 'reportScore', 'achievement','skill','interview','SchoolAcc')  # add this


# Register your models here.
admin.site.register(AdminApp, AdmissionData)  # add this
