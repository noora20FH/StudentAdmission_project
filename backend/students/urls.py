from django.urls import path
from .views import StudentView, StudentUpdateDestoryView

urlpatterns = [
    path("students/", StudentView.as_view()),
    path("students/<int:pk>/", StudentUpdateDestoryView.as_view())
]
