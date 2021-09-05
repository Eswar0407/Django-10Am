from django.shortcuts import render,redirect
from app_db.forms import *
from app_db.models import *

# Create your views here.
def showIndex(request):
    cf = CustomerForm(request.POST)
    if request.method == "POST":
        cf.save()
        return redirect('main')
    else:
        return render(request,'index.html',{"c_form":cf,"c_data":CustomerModel.objects.all()})


def showProduct(request):
    pf = ProductForm(request.POST)
    if request.method == "POST":
        pf.save()
        return redirect('product')
    else:
        return render(request,'product.html', {"p_form": pf, "p_data": ProductModel.objects.all()})


def showOrder(request):
    pf = OrderForm(request.POST)
    if request.method == "POST":
        pf.save()
        return redirect('order')
    else:
        return render(request, 'order.html',{"o_form": pf, "o_data": OrderModel.objects.all()})