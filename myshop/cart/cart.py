from decimal import Decimal
from django.conf import settings
from shop.models import Product


class Cart:
    def __init__(self,request):
        self.sessions = request.sessions
        cart = self.sessions(settings.CART_SESSION_ID)
        if not cart:
            cart = self.sessions[settings.CART_SESSION_ID]={}
        self.cart = cart
        
        
    # add the items for the cart
    def add(self,product,quantity=1,override_quantity=False):
        """
        Add a product to the cart or update its quantity.
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity' : 0,
                'price' : str(product.price)
            }
            
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        
        self.save()
        
    
    # save the cart for the user
    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.sessions.modified = True
        
        
    def remove(self,product):
        """Remove data from the cart"""
        product_id = str(product.id)
        
        # checking
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
            
            
            
    def __iter__(self):
        """Iterate over the items in the cart and get the products
        from the database"""
        product_ids = self.cart.keys()
        # get the product objects and add them to the cart
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
        yield item