from django.shortcuts import render
from app_form.forms import EmployeeRegistrationForm

# Create your views here.
def showIndex(request):
    return render(request,'index.html')


def addEmployee(request):
    emp = EmployeeRegistrationForm()
    return render(request,'add_employee.html',{"form":emp})


def saveEmployee(request):
    id = request.POST.get("idno")
    na = request.POST.get("name")
    sal = request.POST.get("salary")
    desg = request.POST.get("designation")

    return None