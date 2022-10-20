from django.shortcuts import render

from customers.models import Product

# Create your views here.

def seeProducts(request):
    products = Product.objects.all()
    return render(request, 'customers/templates/seeProducts.html', {'products':products})

