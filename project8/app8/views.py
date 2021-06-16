from django.shortcuts import render

def showIndex(request):
    student_info = {"data":
                    [
                    {"Idno":101,"Name": "Eswar","Marks": [88, 59, 22, 48, 66, 95]},
                    {"Idno":102,"Name": "Hima","Marks": [87, 58, 23, 47, 67, 96]},
                    {"Idno":103,"Name": "Bhaskar","Marks": [86, 57, 24, 46, 68, 97]},
                    {"Idno":104,"Name": "Raghu","Marks": [85, 56, 21, 45, 69, 98]},
                    {"Idno":105,"Name": "sunny","Marks": [84, 55, 20, 44, 70, "A"]}
                   ]
                   }
    return render(request,'index.html',student_info)
