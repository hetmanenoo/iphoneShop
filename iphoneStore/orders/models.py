from django.db import models
from catalog.models import Items


class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    data_created = models.DateTimeField(auto_now_add=True)
    data_updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    _id = models.AutoField(primary_key=True, editable=False)

    class Meta:
        ordering = ('-data_created',)
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'

    def __str__(self):
        return f'Order {self._id}'# type: ignore 

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())  # type: ignore 
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.PROTECT)
    product = models.ForeignKey(Items, related_name='order_items', on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)# type: ignore 

    def get_cost(self):
        return self.price * self.quantity
