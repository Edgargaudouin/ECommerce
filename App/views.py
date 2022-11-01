from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from App.models import Product

# Create your views here.

def store(request):
    context = {}
    return render(request, 'store.html', context)

def cart(request):
    context = {}
    return render(request, 'cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'checkout.html', context) 
