from rest_framework import serializers
from .models import Student, AdmissionResult
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('studentId',
                  'FirstName',
                  'LastName',
                  'RegistrationNo',
                  'Email',
                  'Course')
        
class AdmissionResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmissionResult
        fields = ('studentId',
                  'stdName',
                  'c1',
                  'c2',
                  'c3',
                  'c4',
                  'c5'
                  )
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'password')
        extra_kwargs = { 'password': {'write_only': True, 'required': True}}
        
        def create(self, validated_data):
            user = User.objects.create_user(**validated_data)
            Token.objects.create(user=user)
            return user