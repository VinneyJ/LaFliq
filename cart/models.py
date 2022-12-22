from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from fliq.models import Customer, Item



class CartItem(models.Model):
    item = models.OneToOneField(Item, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(default=datetime.now)


    def increment_quantity(self):
        self.quantity += 1

    @property
    def price_VAT_inclusive(self):
        VAT_TAX = 16.0
        if self.quantity > 1:
            tot_price = self.item.price * (100 + VAT_TAX)/100.00
            return tot_price * self.quantity
        else:
            return self.item.price * (100 + VAT_TAX)/100.00

        

    def __str__(self):
        return self.item.title


class Cart(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
    ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now)

    # For getting all the cart items
    def get_all_items(self):
        return self.items.all()

    # Calculate the cart total
    def get_cart_total(self):
        return sum([product.price_VAT_inclusive for product in self.items.all()])