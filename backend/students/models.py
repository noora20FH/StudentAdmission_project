from django.db import models

# Create your models here.


class Student(models.Model):
    studentId = models.AutoField(primary_key=True)
    stdName = models.CharField(max_length=100, default='')
    averageScore = models.CharField(max_length=100)
    achievement = models.CharField(max_length=100)
    skillCertificate = models.CharField(max_length=100)
    testResult = models.CharField(max_length=100)
    schoolName = models.CharField(max_length=100, default='')
    schoolAccreditation = models.CharField(max_length=100)

class AdmissionResult(models.Model):
    studentId = models.AutoField(primary_key=True)
    stdName = models.CharField(max_length=100)
    c1 = models.CharField(max_length=100, default='')
    c2 = models.CharField(max_length=100, default='')
    c3 = models.CharField(max_length=100, default='')
    c4 = models.CharField(max_length=100, default='')
    c5 = models.CharField(max_length=100, default='')
    