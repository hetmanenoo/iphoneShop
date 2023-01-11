from django.shortcuts import render
from orders.models import Order
from cart.cart import Cart

# Create your views here.
def payment_success_page(request, order_id):  
    
    cart = Cart(request)

    # orders = Order.objects.filter(_id=order_id).update(paid = True)
    orders = Order.objects.get(_id=order_id)
   
    orders.paid = True
    orders.save(update_fields=["paid"])

    cart.clear() #очищення корзини
    
    context ={
        'title': 'Оплата',
        
        
    }
    return render(request, 'payment/payment_success.html', context=context)