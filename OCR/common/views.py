from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from student.models import RegistrationModel
from common.utils import sendTextMessage
from random import randint
from django.db.models import Q
from django.contrib import messages
def showCommonPage(request):
    return render(request,"common/index.html")

def studentPage(request):
    return render(request,"common/student.html")

def studentRegistartion(request):
    if request.method == "POST":
        name = request.POST.get("student_name")
        contact = request.POST.get("student_contact")
        email = request.POST.get("student_email")
        password = request.POST.get("student_password")

        record = RegistrationModel.objects.filter(Q(Contact=contact) | Q(Email=email))

        if record:
            return render(request, "common/student.html", {"data": [name, contact, email, "Contact Number or Email is Already Taken"]})
        else:
           otp = randint(100000,999999)

           message = '''Thanks from Registered with Zilla Parishad High School,
            To finish registration use the given OTP
            Your OTP : '''+str(otp)

           if sendTextMessage(message,contact):
                RegistrationModel(Name=name,Contact=contact,Email=email,Password=password,Otp=otp).save()
                messages.success(request,contact)
                return redirect('student_otp')
           else:
             return render(request, "common/student.html", {"data": [name, contact, email, "Wrong Contact Number"]})


    else:
      studentPage(request)

def openStudentOtp(request):
    return render(request,"common/otp.html")

def studentLoginCheck(request):
    if request.method == "POST":
        email = request.POST.get("student_email")
        password = request.POST.get("student_password")
        return HttpResponse("Under Development")
    else:
       return render(request, "common/student.html")

def validateOtp(request):
    contact = request.POST.get("contact")
    sotp = request.POST.get("student_otp")

    try:
        record = RegistrationModel.objects.get(Contact=contact,Otp=sotp)
        record.Status = 'Active'
        record.save()
        return render(request, "common/student.html",{"message":"Thanks for Registaration, Please Login...!"})
        print(result)
    except RegistrationModel.DoesNotExist:
        messages.success(request, contact)
        return redirect('student_otp')






