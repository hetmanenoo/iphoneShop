from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
from catalog.models import Items

from iphoneStore import settings

# Create your models here.
class Cart_items_auth(models.Model):
    # id = models.AutoField(primary_key=True, editable=False, verbose_name='Id')
    user = models.CharField(max_length=255)
    product = models.ForeignKey(Items, on_delete=models.PROTECT)
    quantity = models.CharField(max_length=255 ,default="")
    price = models.CharField(max_length=255)
    # update_quantity = models.CharField(max_length=255 ,default="")

    add_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Товар: {self.product.title}, Користувач ід: {self.user} ..."

class Cart_user(models.Model):

    # _id = models.AutoField(primary_key=True, editable=False, verbose_name='Id')
    total_price = models.CharField(max_length=255)
    total_quantity = models.CharField(max_length=255)
    add_datetime = models.DateTimeField(auto_now_add=True)
    user_id = models.IntegerField()
    
    def __str__(self):
        return f"Корстувач ід: {self.user_id}, Замовив {self.total_quantity}од. на : {self.total_price} грн. "