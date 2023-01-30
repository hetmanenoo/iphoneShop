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
        # 'server_url': 'https://f930-185-12-142-79.eu.ngrok.io/payment/pay-callback/', 
        "result_url": "https://ba27-31-144-105-135.eu.ngrok.io/payment/status/",  #Вставити актуальну силку з ngrok
        
        
    }

    return params
