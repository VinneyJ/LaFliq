from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from fliq.models import Customer, Item, OrderItem, Order, ShippingAddress
# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)


class CartItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.FloatField(blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    

    def price_VAT_inclusive(self):
        VAT_TAX = 16.0
        return self.price * (100 + VAT_TAX)/100.00

    def __str__(self):
        return self.user.email + "-" + self.item