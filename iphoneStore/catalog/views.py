from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *
from cart.forms import CartAddProductForm
from cart.cart import Cart
from cart.cart_auth import Cart_auth


def catalog_page(request):
    products = Items.objects.all()

    context = {}

    if "min_price" in request.GET:
        filter_price1 = request.GET.get("min_price")
        filter_price2 = request.GET.get("max_price")
        context["min_price"] = filter_price1
        context["max_price"] = filter_price2

        if filter_price1 == "":
            filter_price1 = 0
        products = Items.objects.filter(price__range=(filter_price1, filter_price2))

    cats = Category.objects.all()

    paginator = Paginator(products, 5)

    page_numbers = request.GET.get("page")
    page_obj = paginator.get_page(page_numbers)

    cart_product_form = CartAddProductForm()

    cart = Cart(request)

    user = request.user

    cart_auth = Cart_auth(user)

    context.update(
        {
            "cart_auth": cart_auth,
            "cart": cart,
            "cats": cats,
            "title": "Католог",
            "items": products,
            "page_obj": page_obj,
            "cart_product_form": cart_product_form,
        }
    )

    return render(request, "catalog/catalog.html", context=context)


def show_category_page(request, cat_id):

    cats = Category.objects.all()
    products = Items.objects.filter(cat_id=cat_id)

    context = {}

    if "min_price" in request.GET:

        filter_price1 = request.GET.get("min_price")
        filter_price2 = request.GET.get("max_price")

        context["min_price"] = filter_price1
        context["max_price"] = filter_price2

        if filter_price1 == "":
            filter_price1 = 0
        products = Items.objects.filter(
            price__range=(filter_price1, filter_price2), cat_id=cat_id
        )

    paginator = Paginator(products, 5)

    page_numbers = request.GET.get("page")
    page_obj = paginator.get_page(page_numbers)

    cart_product_form = CartAddProductForm()

    cart = Cart(request)

    context.update(
        {
            "cart": cart,
            "cats": cats,
            "title": "Католог",
            "items": products,
            "page_obj": page_obj,
            "cart_product_form": cart_product_form,
        }
    )

    return render(request, "catalog/catalog.html", context=context)


def item_page(request, item_id):

    products = Items.objects.filter(id=item_id)
    cats = Category.objects.all()

    cart = Cart(request)
    cart_product_form = CartAddProductForm()

    context = {
        "cats": cats,
        "title": "Католог",
        "items": products[0],
        "item_selected": item_id,
        "cart": cart,
        "cart_product_form": cart_product_form,
    }

    return render(request, "catalog/item.html", context=context)
