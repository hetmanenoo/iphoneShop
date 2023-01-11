from django.urls import path, re_path
from . import views

app_name = 'payment'

urlpatterns = [
    
    path(r'^success/(?P<order_id>\d+)/$', views.payment_success_page, name='payment_success'),

]