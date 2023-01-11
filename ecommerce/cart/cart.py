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