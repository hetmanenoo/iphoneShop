from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from catalog.models import Items
from catalog.models import Category
from .cart import Cart
from .forms import CartAddProductForm
from django.http import HttpResponseRedirect


@require_POST
def cart_add(request, items_id):
    cart = Cart(request)
    items = get_object_or_404(Items, id=items_id)
    form = CartAddProductForm(request.POST)
    
    cats = Category.objects.all()

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(items=items, quantity=cd['quantity'], update_quantity=cd['update'])
   
    return redirect('cart:cart_detail')
    
    

def cart_remove(request, items_id):
    cart = Cart(request)
    item = get_object_or_404(Items, id=items_id)

    cart.remove(item)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cats = Category.objects.all()
    # cart = Cart(request)
    # products = []
    # infos = []

    # for item in cart:
    #     info = item['items']
    #     item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    #     products.append(item)
    #     infos.append(info)
    #     # print(item['items'])

    # return render(request, 'cart/detail.html', {'cart': cart, 'products': products, 'info': infos})
    cart_product_form = CartAddProductForm()
    cart = Cart(request)

    for item in cart:
        
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
        

    return render(request, 'cart/detail.html', {'cart': cart, 'cats':cats})



@require_POST
def cart_add_home(request, items_id):
    cart = Cart(request)
    items = get_object_or_404(Items, id=items_id)
    form = CartAddProductForm(request.POST)
    
    cats = Category.objects.all()

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(items=items, quantity=cd['quantity'], update_quantity=cd['update'])


    
    # print(request.META.get('HTTP_REFERER', '/'), 3123123)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    # return redirect('cart:cart_detail')
    