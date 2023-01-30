from django.contrib import admin

from .models import Cart_items_auth, Cart_user
# Register your models here.
admin.site.register(Cart_user)

admin.site.register(Cart_items_auth)