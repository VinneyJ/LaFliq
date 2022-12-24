from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, LoginForm

# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'auth/register.html', {'form': form})

from django.contrib.auth import authenticate, login

    def login_view(request):
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user:
                    login(request, user)
                    return redirect('home')
                else:
                    # Return an error message
                    return HttpResponse("Invalid login credentials.")
        else:
            form = LoginForm()
        return render(request, 'auth/login.html', {'form': form})


def home(request):
    items = Item.objects.all()
    context = {'items':items}
    return render(request, 'store/home.html', context)

def cart(request):
   
    return render(request, 'store/cart.html', )

def checkout(request):
    return render(request, 'store/checkout.html')