from django.shortcuts import render
from .models import *


# Create your views here.

def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/index.html', context)


def details(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {'product_details': product}
    return render(request, 'store/product_details.html', context)
