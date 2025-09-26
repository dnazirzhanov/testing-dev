from django.http import HttpResponse
from django.shortcuts import render

def hello_world(request):
    return HttpResponse("Hello, World!")

def homepage(request):
    return render(request, 'homepage.html')
