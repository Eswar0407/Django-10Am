from django.shortcuts import render
from app14.models import Registration

def showMainpage(request):
    return render(request,"main.html")



def showRegisterpage(request):
    if request.method == 'POST':
        n = request.POST.get("name")
        con = request.POST.get("contact")
        mail = request.POST.get("email")
        pswd = request.POST.get("password")
        loc = request.POST.get("location")
        photo = request.FILES["photo"]
        dob = request.POST.get("date")

        Registration(name=n,contact_no=con,email=mail,password=pswd,location=loc,photo=photo,dob=dob).save()

        return render(request,"register.html",{"message":"Registartion is Done"})

    else:
        return render(request,"register.html")



def showLoginpage(request):
    if request.method == 'GET':
        return render(request, "login.html")
    else:
        mail = request.POST.get("email")
        pswd = request.POST.get("password")

        try:
          stu_obj = Registration.objects.get(email=mail, password=pswd)
          return render(request,"enter_login.html")
        except Registration.DoesNotExist:
          return render(request, "login.html", {"error_message": "Invalid User"})


#def enterLoginpage(request):
    #return render(request,"enter_login.html")