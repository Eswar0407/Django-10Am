from django.shortcuts import render

# Create your views here.
def showIndex(request):
    return render(request,"index.html")


def showAbout(request):
    return render(request,"about.html")