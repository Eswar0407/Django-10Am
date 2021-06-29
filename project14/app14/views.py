from django.shortcuts import render

def showMainpage(request):
    return render(request,"main.html")



def showRegisterpage(request):
    return render(request,"register.html")



def showLoginpage(request):
    return render(request,"login.html")