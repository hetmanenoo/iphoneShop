from django.shortcuts import get_object_or_404
from decimal import Decimal
from django.conf import settings
from catalog.models import Items
from .models import Cart_items_auth, Cart_user
from decimal import Decimal


class Cart_auth(object):
    def get_total_price(self, user):
        item = Cart_items_auth.objects.filter(user=user)
        sum = 0

        for i in range(len(item)):
            item_p = item[i].product.price
            item_q = item[i].quantity

            sum = sum + (int(item_p) * int(item_q))

        return sum

    def clear(self, user):

        item = Cart_items_auth.objects.filter(user=user)
        item.delete()

    def len(self, user):
        item = Cart_items_auth.objects.filter(user=user)
        sum = 0

        for i in range(len(item)):
            sum += int(item[i].quantity)

        return sum

    def update_price(self, user, items):
        item = Cart_items_auth.objects.filter(user=user, product=items)

        price = int(items.price) * int(item[0].quantity)

        item.update(price=price)

    # def add_cart(self, user, items, quantity=1):
    def add_cart(self, user, items, quantity=1, update_quantity=False):

        item = Cart_items_auth.objects.filter(user=user, product=items)

        if item:
            if update_quantity:
                item.update(quantity=quantity)
                self.update_price(user, item[0].product)

            else:
                # print( item[0].quantity , ' було')
                quantity_new = int(item[0].quantity) + quantity
                # print(quantity_new, ' стало')
                item.update(quantity=quantity_new)

                self.update_price(user, items)

        else:
            price = int(items.price) * int(quantity)
            Cart_items_auth.objects.create(
                user=user, product=items, quantity=quantity, price=price
            )

        self.get_total_price(user)

    def remove_cart(self, user, items):
        item = get_object_or_404(Cart_items_auth, user=user.id, product=items)
        if item:
            item.delete()

    def __init__(self, user):
        cart_user = Cart_user.objects.filter()

        if cart_user:
            cart_user.update(
                total_price=self.get_total_price(user.id),
                total_quantity=self.len(user.id),
            )
        else:
            Cart_user.objects.create(
                user_id=user.id,
                total_price=self.get_total_price(user.id),
                total_quantity=self.len(user.id),
            )
