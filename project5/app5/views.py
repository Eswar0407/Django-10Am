from django.shortcuts import render

def showIndex(request):
<<<<<<< HEAD
    return render(request,"demo.html")
=======
    return render(request,"index.html")

def loginCheck(request):
    username = request.POST.get("t1")
    password = request.POST.get("t2")

    if username == "Eswar" and password == "Somavarapu":
        return request(request,"welcome.html")
    else:
        return request(request,"error.html")
>>>>>>> e01526900fb7b26f31a5b9d957298f9b577a70e4
