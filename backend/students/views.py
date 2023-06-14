from rest_framework.views import APIView
<<<<<<< HEAD
from .serializers import StudentSerializer, UserSerializer, AdmissionResultSerializer
from django.http.response import JsonResponse
from .models import Student, AdmissionResult
from django.contrib.auth.models import User
=======
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
# import numpy as np

# def dss_mabac():
#     criteria = ['Criteria 1', 'Criteria 2', 'Criteria 3']
#     alternatives = ['Alternative 1', 'Alternative 2', 'Alternative 3', 'Alternative 4']
#     weights = [0.4, 0.3, 0.3]
#     preferences = np.array([
#         [[1, 3, 2, 4], [4, 1, 3, 2], [2, 3, 1, 4], [4, 2, 3, 1]],
#         [[1, 2, 4, 3], [2, 1, 3, 4], [4, 3, 1, 2], [3, 4, 2, 1]],
#         [[1, 2, 3, 4], [3, 1, 4, 2], [2, 4, 1, 3], [4, 3, 2, 1]]
#     ])
#     num_criteria = len(criteria)
#     num_alternatives = len(alternatives)
    
#     # Step 1: Normalize the preference matrix
#     normalized_preferences = np.zeros((num_criteria, num_alternatives, num_alternatives))
#     for i in range(num_criteria):
#         max_value = np.max(preferences[i])
#         min_value = np.min(preferences[i])
#         normalized_preferences[i] = (preferences[i] - min_value) / (max_value - min_value)
    
#     # Step 2: Calculate the weighted normalized matrix
#     weighted_normalized_matrix = np.zeros((num_criteria, num_alternatives, num_alternatives))
#     for i in range(num_criteria):
#         weighted_normalized_matrix[i] = normalized_preferences[i] * weights[i]
    
#     # Step 3: Calculate the relative closeness coefficient
#     relative_closeness_coefficient = np.zeros(num_alternatives)
#     for j in range(num_alternatives):
#         numerator = np.prod(weighted_normalized_matrix[:, :, j], axis=(0, 1))
#         denominator = np.sum(weighted_normalized_matrix[:, :, j])
#         relative_closeness_coefficient[j] = numerator / denominator
    
#     # Step 4: Rank the alternatives based on the relative closeness coefficient
#     rankings = np.argsort(-relative_closeness_coefficient)
    
#     return rankings

# # Example usage


# rankings = dss_mabac()
# print("ranking", rankings) 
# # Print the rankings
# for rank, alternative in enumerate(rankings):
#     print(f"Rank {rank+1}: Alternative {alternative+1}") 
