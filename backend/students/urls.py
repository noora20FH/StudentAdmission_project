from django.urls import path
from django.conf.urls import include
from django.contrib import admin
from .views import UserViewSet, StudentView, StudentUpdateDestoryView, MabacInputView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("admin/", admin.site.urls),
    path("students/", StudentView.as_view()),
    path("students/<int:pk>/", StudentUpdateDestoryView.as_view()),
    path("mabac_input/", MabacInputView.as_view())
]
