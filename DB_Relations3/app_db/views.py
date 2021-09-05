from django.shortcuts import render,redirect
from app_db.forms import EmployeeForm,AccountForm
from app_db.models import EmployeeModel,AccountModel

# Create your views here.
def showIndex(request):
    ef = EmployeeForm(request.POST)
    if request.method == "POST":
        ef.save()
        return redirect('main')
    else:
       return render(request,'index.html',{"e_form":ef,"e_data":EmployeeModel.objects.all()})


def showAccount(request):
    af = AccountForm(request.POST)
    if request.method == "POST":
        if af.is_valid():
          af.save()
          return redirect('account')
        else:
            return render(request, "account.html",{"a_form": af,"a_data": AccountModel.objects.all()})
    else:
       return render(request,"account.html",{"a_form":af,"a_data":AccountModel.objects.all()})