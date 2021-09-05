
from django import forms
from app_db.models import CourseModel,StudentModel

class CourseForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = CourseModel

class StudentForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = StudentModel