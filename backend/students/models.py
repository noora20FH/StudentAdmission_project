from django.db import models

# Create your models here.


class Student(models.Model):
    studentId = models.AutoField(primary_key=True)
    stdName = models.CharField(max_length=100)
    averageScore = models.IntegerField()
    achievement = models.IntegerField()
    skillCertificate = models.IntegerField()
    testResult = models.IntegerField()
    schoolName = models.CharField(max_length=100)
    schoolAccreditation = models.IntegerField()

class AdmissionResult(models.Model):
    result_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=150)
    results = models.DecimalField( max_digits=10, decimal_places=4)
    ranking = models.IntegerField()
    