from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product

from django.http import JsonResponse

# Create your views here.

def cart_summary(request):
    #get Cart object and put it in variable, then return that variable and load the cart-summart template
    cart = Cart(request)

    return render(request, 'cart/cart-summary.html', {'cart': cart})


def cart_add(request):
    #set cart 
    cart = Cart(request)

    #check if ajax request is post, if it is get id and qty from frontend
    #action is lowercase post from ajax
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))

        #find what product is associated with id
        product = get_object_or_404(Product, id=product_id)
        #once product is found call add to cart function and pass in product and qty
        cart.add(product=product, product_qty=product_quantity)

        #update cart quantity using the length function in the cart.py file
        cart_quantity = cart.__len__()

        response = JsonResponse({'qty': cart_quantity})
        return response 

def cart_delete(request):
    #set cart 
    cart = Cart(request)

    #check if ajax request is post, if it is get id from frontend
    #action is lowercase post from ajax
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))

        cart.delete(product=product_id)
        #update cart qty and total
        cart_quantity = cart.__len__()
        cart_total = cart.get_total()

        response = JsonResponse({'total': cart_total, 'qty': cart_quantity})

        return response



def cart_update(request):
    pass


