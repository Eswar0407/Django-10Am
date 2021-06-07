from django.shortcuts import render
from django.http import HttpResponse

def three(request):
    message = "hello this is the Django project3 Example"
    return HttpResponse(message)
