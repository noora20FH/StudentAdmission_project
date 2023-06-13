from django.urls import path
from django.conf.urls import include
from .views import UserViewSet, GetUserProfileView, UpdateUserProfileView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user', GetUserProfileView.as_view()),
    path('update', UpdateUserProfileView.as_view()),
]
