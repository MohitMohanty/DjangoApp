from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products':products})


def new(request):
    return render(request, 'newPage.html')
# Create your views here.
