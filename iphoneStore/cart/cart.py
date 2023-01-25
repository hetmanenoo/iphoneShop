from decimal import Decimal
from django.conf import settings
from catalog.models import Items



class Cart(object):

    def __init__(self, request):
       
        self.session = request.session
        
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, items, quantity=1, update_quantity=False):
        
        items_id = str(items.id)
        if items_id not in self.cart:
            self.cart[items_id] = {'quantity': 0,
                                    'price': str(items.price)}
        if update_quantity:
            self.cart[items_id]['quantity'] = quantity
        else:
            self.cart[items_id]['quantity'] += quantity
        self.save()

    def save(self):
        
        self.session[settings.CART_SESSION_ID] = self.cart
       
        self.session.modified = True

    def remove(self, items):
        
        items_id = str(items.id)
        if items_id in self.cart:
            del self.cart[items_id]
            self.save()
    
    def __iter__(self):
        
        items_ids = self.cart.keys()
        
        itemses = Items.objects.filter(id__in=items_ids)
        for item in itemses:
            self.cart[str(item.id)]['items'] = item # type: ignore #problem 
            


        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']

            yield item
            
    
    def __len__(self):
        
        return sum(item['quantity'] for item in self.cart.values())
    

    def get_total_price(self):
    
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    

    def clear(self):
       
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True