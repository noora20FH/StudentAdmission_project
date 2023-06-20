from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.authtoken.views import obtain_auth_token
from django.views.generic import TemplateView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('accounts.urls')),
    path('profile/', include('users.urls')),
    
    path('admin/', admin.site.urls),
    path('api/', include('students.urls')),
    path('auth/', obtain_auth_token),
]

urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name = 'index.html'))]