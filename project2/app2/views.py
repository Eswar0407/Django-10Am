from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    message = "hello guys , This is Django Class"
    return HttpResponse(message)

