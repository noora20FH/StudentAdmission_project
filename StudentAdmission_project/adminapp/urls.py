#create this page to make the path 
from django.urls import path
from . import views

#URLConf
# every app can have its configuration
# import the URLConf into the main url of this project in the Project Folder in urls.py file
urlpatterns = [
    path('hello/', views.say_hello),
]