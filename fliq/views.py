from django.shortcuts import render

#Create Class-based views
from django.views.generic import ListView,DetailView
from .models import Item, Order, OrderItem

class HomeView(ListView):
    model = Item
    template_name = 'home.html'


# Create your views here.
def home(request):
    return render(request, 'store/home.html')

def cart(request):
    return render(request, 'store/cart.html')

def checkout(request):
    return render(request, 'store/checkout.html')