from django.shortcuts import render
from .cart import Cart

from .models import Product

# Create your views here.
def home_page(request):
    return render(request, 'index.html')


def add_to_cart(request, slug):

    product = Product.objects.get(slug=slug)
    print(f'PRODUCT IS {product}')

    cart = Cart(request)
    cart.add(product)

    return render(request, 'cart_menu.html', {'cart': cart})

def increment_cart(request, slug):
    product = Product.objects.get(slug=slug)
    cart = Cart(request)
    

    if request.method == 'POST':
        cart.increment(product)

    return render(request, 'cart.html')

def decrement_cart(request, slug):
    product = Product.objects.get(slug=slug)
    cart = Cart(request)

    if request.method == 'POST':
        cart.decrement(product)

    return render(request, 'cart.html')

def remove_from_cart(request, slug):
    product = Product.objects.get(slug=slug)
    cart = Cart(request)

    cart.remove(product)

    return render(request, 'cart.html')