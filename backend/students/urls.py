from django.urls import path
from django.conf.urls import include
from django.contrib import admin
from .views import UserViewSet, StudentView, StudentUpdateDestoryView, MabacInputView
from rest_framework import routers

urlpatterns = [
    path('', include(router.urls)),
    path("admin/", admin.site.urls),
    path("students/", StudentView.as_view()),
    path("students/<int:pk>/", StudentUpdateDestoryView.as_view()),
    path("mabac/", MabacCalculation.as_view()),
    path("save/", SaveMabacResult.as_view()),
]
