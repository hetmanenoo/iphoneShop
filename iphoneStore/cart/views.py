from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from catalog.models import Items
from catalog.models import Category

from .cart import Cart
from .models import Cart_items_auth, Cart_user
from .cart_auth import Cart_auth
from .forms import CartAddProductForm, CartUpdateProductForm

from django.http import HttpResponseRedirect


@require_POST
def cart_add(request, items_id):
    cart = Cart(request)
    items = get_object_or_404(Items, id=items_id)
    form = CartAddProductForm(request.POST)

    cats = Category.objects.all()

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(items=items, quantity=cd["quantity"], update_quantity=cd["update"])

    return redirect("cart:cart_detail")


def cart_remove(request, items_id):
    cart = Cart(request)
    item = get_object_or_404(Items, id=items_id)

    cart.remove(item)
    return redirect("cart:cart_detail")


def cart_detail(request):
    cats = Category.objects.all()
    cart_product_form = CartAddProductForm()
    cart = Cart(request)

    for item in cart:

        item["update_quantity_form"] = CartAddProductForm(
            initial={"quantity": item["quantity"], "update": True}
        )

    return render(request, "cart/detail.html", {"cart": cart, "cats": cats})


@require_POST
def cart_add_home(request, items_id):

    cart = Cart(request)
    items = get_object_or_404(Items, id=items_id)

    form = CartAddProductForm(request.POST)

    # cats = Category.objects.all()

    # form_up = CartUpdateProductForm()

    if form.is_valid():

        cd = form.cleaned_data
        cart.add(items=items, quantity=cd["quantity"], update_quantity=cd["update"])

    # print(request.META.get('HTTP_REFERER', '/'), 3123123)
    return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))
    # return redirect('cart:cart_detail')


def cart_detail_auth(request):

    user = request.user
    cart = Cart_auth(user)

    items = Cart_items_auth.objects.filter(user=user.id)

    user_cart = Cart_user.objects.filter(user_id=user.id)

    total_price = cart.get_total_price(user=user.id)

    form = CartAddProductForm()

    form1 = CartAddProductForm(request.POST)

    return render(
        request,
        "cart/detail_auth.html",
        {
            "cart": items,
            "total_price": total_price,
            "user_cart": user_cart[0],
            "form": form,
            "form1": form1,
        },
    )


@require_POST
def cart_add_auth(request, items_id):

    items = get_object_or_404(Items, id=items_id)

    user = request.user
    cart = Cart_auth(user)

    form = CartAddProductForm(request.POST)
    form1 = CartUpdateProductForm(request.POST)

    # cart.add_cart(user = user.id ,items = items)

    if form.is_valid():
        cd = form.cleaned_data

        cart.add_cart(
            user=user.id,
            items=items,
            quantity=cd["quantity"],
            update_quantity=cd["update"],
        )

    # if form1.is_valid():
    #     cd = form.cleaned_data
    #     cart.add_cart(user = user.id, items=items, quantity=cd['quantity'], update_quantity=cd['update'])

    return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))


@require_POST
def cart_add_update_auth(request, items_id):

    items = get_object_or_404(Items, id=items_id)

    user = request.user
    cart = Cart_auth(user)

    form1 = CartUpdateProductForm(request.POST)
    if form1.is_valid():
        cd = form1.cleaned_data
        cart.add_cart(
            user=user.id, items=items, quantity=cd["quantity"], update_quantity=True
        )

    return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))


def cart_remove_auth(request, items_id):
    user = request.user
    # item = get_object_or_404(Items, id=items_id)

    cart = Cart_auth(user=user)

    cart.remove_cart(user=user, items=items_id)

    return redirect("cart:cart_detail_auth")
