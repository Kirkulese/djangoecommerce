from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product

from django.http import JsonResponse

# Create your views here.

def cart_summary(request):
    return render(request, 'cart/cart-summary.html')


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

        response = JsonResponse({'the product is called: ': product.title, ' and the qty is: ': product_quantity})
        return response 

def cart_delete(request):
    pass


def cart_update(request):
    pass


