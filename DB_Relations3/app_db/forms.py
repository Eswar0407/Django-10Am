from django import forms
from app_db.models import EmployeeModel,AccountModel

class EmployeeForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = EmployeeModel

class AccountForm(forms.ModelForm):
     def visible_fields(self):
        return True
     class Meta:
         fields = "__all__"
         model = AccountModel