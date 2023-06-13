from django.urls import path
from django.conf.urls import include
from django.contrib import admin
from .views import UserViewSet, StudentView, StudentUpdateDestoryView, MabacInputView
from .views import StudentView, StudentUpdateDestoryView
from rest_framework import routers

urlpatterns = [
    path("students/", StudentView.as_view()),
    path("students/<int:pk>/", StudentUpdateDestoryView.as_view()),
    path("mabac_input/", MabacInputView.as_view())
]
