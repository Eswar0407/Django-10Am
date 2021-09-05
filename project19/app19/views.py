from django.shortcuts import render
from app19.forms import FileUploadingForm,FileModel

# Create your views here.
def showIndex(request):
    return render(request,"index.html",{"form":FileUploadingForm(),"data":FileModel.objects.all()})


def saveFile(request):
    FileModel(name=request.POST.get('name'),file=request.FILES['file']).save()
    return showIndex(request)