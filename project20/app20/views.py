from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def showIndex(request):
    return render(request, 'index.html')

    # if request.method == "POST":
     #   return render(request,'index.html')
    #if request.method == "GET":
     #   return HttpResponse("am Get")


def openSave(request):
    if request.method=="POST":
        return HttpResponse("am post")
    else:
        return HttpResponse("am get")