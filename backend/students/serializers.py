from rest_framework import serializers
from .models import Student, AdmissionResult


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('studentId',
                  'FirstName',
                  'LastName',
                  'RegistrationNo',
                  'Email',
                  'Course')
class AdmissionResult(serializers.ModelSerializer):
    class Meta:
        model = AdmissionResult
        fields = ('studentId',
                  'stdName',
                  'admsResult')