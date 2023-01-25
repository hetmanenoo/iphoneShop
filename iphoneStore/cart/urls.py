from django.urls import include, path, re_path
from . import views

app_name = "cart"

urlpatterns = [
    re_path(r"^$", views.cart_detail, name="cart_detail"),
    re_path(r"^add/(?P<items_id>\d+)/$", views.cart_add_home, name="cart_add_home"),
    # re_path(r'^add/(?P<items_id>\d+)/$', views.cart_add, name='cart_add'),
    re_path(r"^remove/(?P<items_id>\d+)/$", views.cart_remove, name="cart_remove"),
    re_path(r"^auth/$", views.cart_detail_auth, name="cart_detail_auth"),
    re_path(
        r"^remove_auth/(?P<items_id>\d+)/$",
        views.cart_remove_auth,
        name="cart_remove_auth",
    ),
    re_path(
        r"^add_auth/(?P<items_id>\d+)/$", views.cart_add_auth, name="cart_add_auth"
    ),
    re_path(
        r"^up_add_auth/(?P<items_id>\d+)/$",
        views.cart_add_update_auth,
        name="cart_add_update_auth",
    ),
]
