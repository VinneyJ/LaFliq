from django.contrib import admin
from .models import Customer,Item, Order, OrderItem, ShippingAddress

#Define item display
class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    list_display = [
        'title',
        'price',
        'discount_price',
        'description'
    ]

#Register models
admin.site.register(Customer)
admin.site.register(Item, ItemAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)


