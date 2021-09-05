from django.shortcuts import render,redirect
from app_db.forms import StudentForm,CourseForm
from app_db.models import StudentModel,CourseModel
# Create your views here.
def showIndex(request):
    course = CourseForm(request.POST)
    if request.method == "POST":
        course.save()
        return redirect('main')
    else:
       return render(request,'index.html',{"c_form":course,"all_courses":CourseModel.objects.all()})


def showStudent(request):
    student = StudentForm(request.POST)
    if request.method == "POST":
        student.save()
        return redirect('student')
    else:
      result = CourseModel.objects.all()
      if result:
        return render(request,"student.html",{"s_form": StudentForm(),"all_students":StudentModel.objects.all()})
      else:
        return render(request,"student.html",{"error":"Please Add The Course...!"})