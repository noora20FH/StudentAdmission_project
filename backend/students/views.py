from rest_framework.views import APIView
from .serializers import StudentSerializer, AdmissionResultSerializer
from django.http.response import JsonResponse
from .models import Student, AdmissionResult
from django.contrib.auth.models import User
from django.http.response import Http404
from rest_framework.response import Response
from rest_framework import generics, viewsets
import numpy as np
from scipy.stats import rankdata

class Login(generics.ListCreateAPIView):
    pass

class StudentCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentUpdateDestoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

def calculate_ranks():
    # Define Student Matrix and corresponding alternatives
    students = Student.objects.all()
    if not students:
        print("No student data")
    else:
        student_names = [student.stdName for student in students]
        print("Students", student_names)
        student_matrix = np.array([
            [student.averageScore for student in students],
            [student.achievement for student in students],
            [student.skillCertificate for student in students],
            [student.testResult for student in students],
            [student.schoolAccreditation for student in students],
        ]).T

    # Call the function for calculation
    criteria_types = np.array(["benefit", "benefit", "benefit", "benefit", "benefit"])
    weights = np.array([30, 20, 20, 15, 15])

    # Step 1: Create the decision matrix
    print("Decision Matrix:")
    print(student_matrix)

    # Step 2: Normalize the decision matrix and get max and min values for each criterion
    max_values = np.amax(student_matrix, axis=0)
    min_values = np.amin(student_matrix, axis=0)
    print('Max', max_values)
    print('Min', min_values)
    print("student", student_matrix.shape[0])
    normalized_matrix = np.zeros(student_matrix.shape)
    for i in range(student_matrix.shape[1]):
        if criteria_types[i] == "Cost":
            normalized_matrix[:, i] = (max_values[i] - student_matrix[:, i]) / (max_values[i] - min_values[i])
        else:
            normalized_matrix[:, i] = (student_matrix[:, i] - min_values[i]) / (max_values[i] - min_values[i])

    print("Normalized Matrix:")
    print(normalized_matrix)



    # Step 3: Calculate the weighted normalized decision matrix for the decision maker
    normalized_weights = weights / np.sum(weights)

    weighted_matrix = (normalized_matrix * normalized_weights.reshape(1, -1)) + normalized_weights.reshape(1, -1)

    print("Weighted Normalized Matrix:")
    print(weighted_matrix)

    # Step 4: Calculate the approximate boundary area matrix (G)
    product = np.prod(weighted_matrix, axis=0)
    G = product ** (1 / weighted_matrix.shape[0])

    print("G:")
    print(G)

    # Step 5: Calculate the alternative distance matrix from the approximate boundary area (Q)
    Q = weighted_matrix - G.reshape(1, -1)

    print("Q:")
    print(Q)

    # Step 6: Calculate the alternative rankings
    S = np.sum(Q, axis=1)
    for i in S:
        print("Si", i)
    # Calculate the ranks using scipy.stats.rankdata with the 'min' method for ties
    ranks = rankdata(-S, method='min')

    # Create a list of alternatives with their corresponding S values and ranks
    alternative_rankings = [(name, '{:.4f}'.format(s), rank) for name, s, rank in zip(student_names, S, ranks)]

    return alternative_rankings


result = calculate_ranks()

for name, s, rank in result:
    print(f'{name}: {s}, {rank}')


class MabacCalculation(generics.ListCreateAPIView):
    queryset = AdmissionResult.objects.all()
    serializer_class = AdmissionResultSerializer
    

class SaveMabacResult(APIView):
    queryset = AdmissionResult.objects.all()
    serializer_class = AdmissionResultSerializer

    def get(self, request):
        # Call the function to get the calculation results
        alternative_rankings = calculate_ranks()

        for name, s, rank in alternative_rankings:
            # Check if the data already exists in the database
            if AdmissionResult.objects.filter(student_name=name).exists():
                return Response({"message": "Data already exists."})

            # Save the data to the table
            mabac = AdmissionResult(student_name=name, results=s, ranking=rank)
            mabac.save()

        return Response({"message": "Calculation successfully."})
