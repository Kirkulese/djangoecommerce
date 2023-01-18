#this cart.py file will contain all the cart functions 
class Cart():
    #initialize session when creating cart
    def __init__(self, request):
        #initialize session object from existing user 
        self.session = request.session
        #find the session key within the session object
        cart = self.session.get('session_key')
        
        #if no existing session, create new session key
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        #assign cart to self
        self.cart = cart
    
    def add(self, product, product_qty):
        
        #find product id, check if item is in cart, if it is change qty. otherwise add it to cart with price and qty
        product_id = str(product.id)

        if product_id in self.cart:
            self.cart[product_id]['qty'] = product_qty
        
        else:
            self.cart[product_id] = {'price': str(product.price), 'qty': product_qty}


        #track that session has been modified
        self.session.modified = True
