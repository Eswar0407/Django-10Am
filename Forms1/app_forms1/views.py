from django.shortcuts import render
from app_forms1.forms import EmployeeRegistrationForm
from app_forms1.models import EmployeeRegistrationModel

# Create your views here.
def showIndex(request):
    return render(request,'index.html')


def addEmployee(request):
    #emp = EmployeeRegistrationForm(request.POST)
    emp = EmployeeRegistrationForm()
    if request.method == "POST":
      na = request.POST.get("name")
      con = request.POST.get("contact")
      sal = request.POST.get("salary")
      desg = request.POST.get("designation")
      dob = request.POST.get("dob")
      email = request.POST.get("email")
      EmployeeRegistrationModel(name=na,contact=con,salary=sal,designation=desg,dob=dob,email=email).save()
      #emp.save()
      return render(request, 'add_employee.html', {"form": emp})
    else:
        return render(request,'add_employee.html',{"form":emp})