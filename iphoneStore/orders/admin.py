from django.contrib import admin
from .models import *
# Register your models here.




class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['_id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'data_created', 'data_updated']
    list_filter = ['paid', 'data_created', 'data_updated']
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)