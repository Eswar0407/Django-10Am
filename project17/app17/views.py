from django.shortcuts import render,redirect
from app17.models import ProductModel

# Create your views here.
def showMainpage(request):
    if request.method == "POST":
        name = request.POST.get("product_name")
        price = request.POST.get("product_price")
        photo = request.FILES['product_photo']
        ProductModel(name=name,price=price,photo=photo).save()
        return redirect('main')
    else:
        return render(request,'index.html')


def viewAll(request):
    products_list = ProductModel.objects.all()

    if request.COOKIES.get("csrftoken"):
        total_cookies = len(request.COOKIES) - 1

    else:
       total_cookies = len(request.COOKIES)
    return render(request,"viewall.html",{"All_products":products_list,"cookie":total_cookies})


def saveCookie(request):
    product_number = request.GET.get("pno")
    product_name = request.GET.get("pname")
    response = redirect("view_all")
    response.set_cookie(product_number,product_name)
    return response