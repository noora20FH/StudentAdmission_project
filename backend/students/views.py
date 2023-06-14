from rest_framework.views import APIView
from .serializers import StudentSerializer, UserSerializer, AdmissionResultSerializer
from django.http.response import JsonResponse
from .models import Student, AdmissionResult
from django.contrib.auth.models import User
from .serializers import StudentSerializer
from django.http.response import JsonResponse
from .models import Student
from django.http.response import Http404
from rest_framework.response import Response
from rest_framework import generics
from utils.mabac import dss_mabac

class StudentView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentUpdateDestoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MabacInputView(generics.ListCreateAPIView):
    queryset = AdmissionResult.objects.all()
    serializer_class = AdmissionResultSerializer