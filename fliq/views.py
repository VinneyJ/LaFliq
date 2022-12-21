from django.shortcuts import render, redirect
from .models import *

# Create your views here.


def home(request):
    items = Item.objects.all()
    context = {'items':items}
    return render(request, 'store/home.html', context)

def cart(request):
   
    return render(request, 'store/cart.html', )

def checkout(request):
    return render(request, 'store/checkout.html')