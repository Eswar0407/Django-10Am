from django.shortcuts import render
from django.http import HttpResponse

def showIndex(request):
    message = "Hello sir"
    return HttpResponse(message)


