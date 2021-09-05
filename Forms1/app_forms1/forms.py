from django import forms
from app_forms1.models import EmployeeRegistrationModel

class EmployeeRegistrationForm(forms.ModelForm):
    desg = (
            ('Manager','MANAGER'),
            ('Developer','DEVELOPER'),
            ('Qa','QA'),
           )
    salary = forms.FloatField(min_value=10000)
    designation = forms.ChoiceField(choices=desg)


    class Meta:
       model = EmployeeRegistrationModel
       fields = "__all__"
       labels = {"dob":"Date Of Birth"}