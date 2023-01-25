from django.urls import include, re_path

from .views import PayCallbackView

app_name = "payment"

urlpatterns = [
    re_path(r"^status/$", PayCallbackView.as_view(), name="pay_sucsees"),
]
