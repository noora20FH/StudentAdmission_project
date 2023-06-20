from rest_framework import serializers
from .models import Student, AdmissionResult

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('stdName',
                  'averageScore',
                  'achievement',
                  'skillCertificate',
                  'testResult',
                  'schoolName',
                  'schoolAccreditation')
        
class AdmissionResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmissionResult
        fields = ('student_name', 'results', 'ranking')