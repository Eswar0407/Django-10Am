from django import forms
from app19.models import FileModel
class FileUploadingForm(forms.ModelForm):
    class Meta:
        model = FileModel
        fields = "__all__"