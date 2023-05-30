from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def say_hello(request): 
    # return HttpResponse('Hello Noora!')
    # instead of returning http response, we use render to render http markup in templates folder
    return render(request, 'hello.html', {'name': 'Noora'})

