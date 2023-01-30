from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_POST
from catalog.models import *
from cart.cart import Cart


# phone_info.objects.all() - Всі обєкти з бази даних з таблиці phone_info

# Create your views here.
def base_page(request):
    cats = Category.objects.all()
    cart = Cart(request)

    context = {
        "title": "Головна сторінка",
        "cats": cats,
        "items": Items.objects.all()[0:5],
        "cart": cart,
    }
    return render(request, "mainsite/home.html", context=context)
    # return render(request, 'mainsite/home.html')


def profile_user(request):
    cats = Category.objects.all()
    cart = Cart(request)

    context = {
        "title": "Профіль",
        "cats": cats,
        "items": Items.objects.all()[0:5],
        "cart": cart,
    }
    return render(request, "mainsite/profile.html", context=context)
