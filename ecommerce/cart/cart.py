from decimal import Decimal
from store.models import Product

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

    def delete(self, product):
        product_id = str(product)

        if product_id in self.cart:
            del self.cart[product_id]
        
        self.session.modified = True

        

    def __len__(self):
        #add up all the qty for each item in shopping cart
        return sum(item['qty'] for item in self.cart.values())


    #without this iter class, you cannot use for item in cart statement will return error not iterable    
    def __iter__(self):
        #get all product ids which are the keys, the get products from db by id in cart
        all_product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=all_product_ids)
        
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total'] = item['price'] * item['qty']

            yield item

    def get_total(self):
        #convert price to decimal, multiply by qty for each item in cart
        return sum(Decimal(item['price']) * item['qty'] for item in self.cart.values())