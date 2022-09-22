from django.shortcuts import render

#Create Class-based views
from django.views.generic import ListView,DetailView
from .models import Customer, Item, Order, OrderItem

# Create your views here.
def home(request):
    return render(request, 'store/home.html')

def cart(request):
    return render(request, 'store/cart.html')

def checkout(request):
    return render(request, 'store/checkout.html')