from django.shortcuts import render

def showIndex(request):
    emp_info = {"Idno" : 101,"Name" : "Eswar", "Salary" : 185000.00, "year of experience" : 2}

    return render(request,'index.html',emp_info)