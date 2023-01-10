from django.contrib import admin
from django.urls import include, path

from .views import *

# app_name = 'catalog'

urlpatterns = [
    path('', catalog_page, name='catalog'),
    # path('', catalog_filtre_page, name='catalog_filtre'),
    path(r'^orders/', include('orders.urls', namespace='orders')),
    path('<int:cat_id>/', show_category_page, name='catalog_filter'),
    path('item/<int:item_id>', item_page, name='item_page' )
]
