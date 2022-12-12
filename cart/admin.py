from django.contrib import admin
from .models import Cart, CartItem


#Register models
admin.site.register(Cart)
admin.site.register(CartItem)
