from django.views import View
from .liqpay import LiqPay
from iphoneStore.settings import LIQPAY_PUBLIC_KEY, LIQPAY_PRIVATE_KEY
from django.shortcuts import redirect

from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from orders.models import Order
from cart.models import Cart_items_auth, Cart_user
from cart.cart_auth import Cart_auth


@method_decorator(csrf_exempt, name="dispatch")
class PayCallbackView(View):
    def post(self, request, *args, **kwargs):
        print(LIQPAY_PUBLIC_KEY, LIQPAY_PRIVATE_KEY)
        liqpay = LiqPay(LIQPAY_PUBLIC_KEY, LIQPAY_PRIVATE_KEY)
        data = request.POST.get("data")
        signature = request.POST.get("signature")
        sign = liqpay.str_to_sign(LIQPAY_PRIVATE_KEY + data + LIQPAY_PRIVATE_KEY)

        if sign == signature:
            print("callback is valid")
        response = liqpay.decode_data_from_str(data)
        print("status: ", response["status"])
        print(response)

        if response["status"] == "success" and response["action"] == "pay":
            user = request.user

            # Позначення оплати в БД
            order = Order.objects.filter(_id=response["order_id"])
            order.update(paid=1)

            # Очищення корзини не працює в ngrok бо там user=anonymuser 
            item = Cart_items_auth.objects.filter(user=user)
            item.delete()
           
        else:
           
            print("Упссс")

        if response["status"] == "success":
            return render(request, "payment/payment_success.html")
        else:
            return render(request, "payment/pay_un_sucsees.html")
