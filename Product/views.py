from django.http.response import HttpResponse
from django.shortcuts import render
from . models import Product
from math import ceil

# Create your views here.
def index(request):
    products= Product.objects.all()
    n= len(products)
    nSlides= n//4 + ceil((n/4) + (n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'product': products}
    return render(request,"product/index.html", params)