from django.shortcuts import render, redirect
from django.views import View
from .models import *
from myapp.views import Product




class CreateView(View):
    def get(self, request):
        return render(request, 'create.html')
    

def product(request):
   
    return render(request, 'product.html')



def cart(request):
    cart_items = request.session.get('cart', {})
    products = []
    total = 0
    
    for product_id, quantity in cart_items.items():
        product = Product.objects.get(id=product_id)
        products.append({'product': product, 'quantity': quantity})
        total += product.price * quantity
    
    return render(request, 'cart.html', {'products': products, 'total': total})

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart[product_id] = cart.get(product_id, 0) + 1
    request.session['cart'] = cart
    return render(request,'cart')


 

def footer( request):
        return render(request, 'footer.html') 

