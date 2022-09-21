from django.db import models
from django.contrib.auth.models import User

#define category choices
CATEGORY_CHOICES = (
    ('S', 'Shirts'),
    ('H', 'Hoodies'),
    ('SW', 'Sweatpant')

)
# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField(max_length=200,null=True,blank=True)
    discount_price = models.IntegerField(blank=True, null=True)
    slug = models.SlugField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=200,default="p")

    def __str__(self):
        return self.title

class OrderItem(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()

    def __str__(self):
        return self.user.username