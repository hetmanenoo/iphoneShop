from payment.liqpay import LiqPay
from iphoneStore.settings import LIQPAY_PRIVATE_KEY, LIQPAY_PUBLIC_KEY


def payment_params(
    price,
    order_id,
):

    
    params = {
        "action": "pay",
        "amount": price,  # cart_value, / price
        "currency": "UAH",
        "description": "Payment in IphoneStore",
        "order_id": order_id,  # type: ignore
        "version": "3",
        "sandbox": 0,  # sandbox mode, set to 1 to enable it
        # 'server_url': 'https://f930-185-12-142-79.eu.ngrok.io/payment/pay-callback/', # url на який йде post запрос з даними про статус оплати call-back
        "result_url": "https://d774-185-12-142-69.eu.ngrok.io/payment/status/",  # сторінка редіректа після оплати + callback post з статусом
    }

    return params
