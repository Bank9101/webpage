from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def products(request):
    return render(request, 'products.html')

def product_info(request):
    return render(request, 'product-info.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def topup(request):
    return render(request, 'topup.html')

def sales(request):
    return render(request, 'sales.html')
