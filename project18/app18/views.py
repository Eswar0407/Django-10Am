from django.shortcuts import render,redirect
from app18.models import StudentDetailsModel

# Create your views here.
def showIndex(request):
    return render(request,'index.html')


def saveStudent(request):
    if request.method == "POST":
        name = request.POST.get("name")
        contact = request.POST.get("contact")
        photo = request.FILES['photo']
        dob = request.POST.get('dob')
        email = request.POST.get("email")
        password = request.POST.get("password")

        StudentDetailsModel(name=name,contact=contact,photo=photo,dob=dob,email=email,password=password).save()
        return redirect("main")


def showAdmin(request):
    # details = StudentDetailsModel.objects.all() #we can write this type also
    return render(request,'admin.html',{"students_info":StudentDetailsModel.objects.all()})


def delCandidate(request,student_number):
    student_data = StudentDetailsModel.objects.get(number=student_number)
    if request.method == "POST":
       student_data.delete()
       return render(request,'admin.html',{"students_info":StudentDetailsModel.objects.all()})
    else:
        return render(request,"delete_student.html",{"student_info":student_data})


def updateCandidate(request):
    student_data = StudentDetailsModel.objects.all()
    if request.method == "POST":
        student_data.update()
        return render(request, 'admin.html', {"students_info": StudentDetailsModel.objects.all()})
    else:
        return render(request, "update.html", {"student_info": student_data})