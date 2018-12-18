from django.shortcuts import render

# Create your views here.
from shop.models import Product, Category


def home(request):
    products = Product.objects.filter(active=True)
    categories = Category.objects.filter(active=True)
    context = {"products":products, "categories":categories}
    return render(request, "shop/home.html", context)


def detail(request, slug):
    product = Product.objects.get(active=True, slug=slug)
    context = {"product" : product}
    return render(request, "shop/detail.html", context)
