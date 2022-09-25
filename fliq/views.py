from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    items = Item.objects.all()
    context = {'items':items}
    return render(request, 'store/home.html', context)

def cart(request):
    if request.user.is_authenticated:
        user = request.user.customer
        order, created = Order.objects.get_or_create(username=user)
        items = order.orderitem_set.all()
    else:
        items = []
    context = {'items':items} 
    return render(request, 'store/cart.html', context)

def checkout(request):
    return render(request, 'store/checkout.html')