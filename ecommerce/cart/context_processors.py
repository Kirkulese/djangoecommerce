from .cart import Cart


#this is a helper function to initialize a new Cart with the user request 
#see settings.py to see where this is added to context

def cart(request):
    return {'cart': Cart(request)}