from django.shortcuts import render

def showIndex(request):
    student_info = {"data":
                    [
                    {"Idno":101,"Name": "Eswar","Marks": [88, "A", 22, 48, 66, 95]},
                    {"Idno":102,"Name": "Hima","Marks": [87, 58, 35, "A", 67, 34]},
                    {"Idno":103,"Name": "Bhaskar","Marks": [8, 57, 42, 46, 86, 97]},
                    {"Idno":104,"Name": "Raghu","Marks": [85, 56, 21, 45, 69, 98]},
                    {"Idno":105,"Name": "Sunny","Marks": [84, 55, 70, 44, 20, "A"]},
                    {"Idno":106,"Name": "Naveen","Marks": [48, 25, 50, "A", 20, 34]}
                   ]
                   }
    return render(request,'index.html',student_info)
