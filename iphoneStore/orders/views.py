from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from cart.cart_auth import Cart_auth
from cart.models import Cart_items_auth, Cart_user
from payment.liqpay import LiqPay
from iphoneStore.settings import LIQPAY_PRIVATE_KEY, LIQPAY_PUBLIC_KEY

from .payment_set import payment_params


def order_create(request):

    if request.user.is_authenticated:
        cart = Cart_items_auth.objects.filter(user=request.user.id)

        form = OrderCreateForm

        user = request.user
        cart_auth = Cart_auth(user)
        total_price = cart_auth.get_total_price(user=user.id)

        if request.method == "POST":
            form = OrderCreateForm(request.POST)
            if form.is_valid():
                order = form.save()

                for item in cart:

                    OrderItem.objects.create(
                        order=order,
                        product=item.product,
                        price=item.price,
                        quantity=item.quantity,
                    )

            user = request.user

            user_cart = Cart_user.objects.filter(user_id=user.id)  # type: ignore
            cart_value = user_cart[0].total_price

            liqpay = LiqPay(LIQPAY_PUBLIC_KEY, LIQPAY_PRIVATE_KEY)
            signature = liqpay.cnb_signature(payment_params(cart_value, order._id))  # type: ignore
            data = liqpay.cnb_data(payment_params(cart_value, order._id))  # type: ignore

            return render(request, "payment/payment.html", {"order": order, "id": order._id, "total_price": total_price, "signature": signature, "data": data})  # type: ignore

        else:

            form = OrderCreateForm
            return render(
                request,
                "orders/create.html",
                {
                    "cart": cart,
                    "form": form,
                    "total_price": total_price,
                },
            )

    else:
        cart = Cart(request)

        if request.method == "POST":
            form = OrderCreateForm(request.POST)
            if form.is_valid():
                order = form.save()

                for item in cart:
                    print(item)
                    OrderItem.objects.create(
                        order=order,
                        product=item["items"],
                        price=item["price"],
                        quantity=item["quantity"],
                    )

                return render(
                    request, "payment/payment.html", {"order": order, "id": order._id}
                )

        else:

            form = OrderCreateForm
        return render(request, "orders/create.html", {"cart": cart, "form": form})
