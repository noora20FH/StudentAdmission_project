from django.urls import path
from django.conf.urls import include
from django.contrib import admin
from .views import StudentCreateView, StudentUpdateDestoryView, MabacCalculation, Login, SaveMabacResult
from rest_framework import routers

urlpatterns = [
    path('', Login.as_view()),
    path("students/", StudentCreateView.as_view()),
    path("students/<int:pk>/", StudentUpdateDestoryView.as_view()),
    path("mabac/", MabacCalculation.as_view()),
    path("save/", SaveMabacResult.as_view()),
]
