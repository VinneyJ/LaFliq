from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib import messages
from django.urls import reverse


from fliq.models import Customer, Item
from cart.models import Cart, CartItem



def add_to_cart(request, id_unique):
    """
    1. Get the user instance
    2. Get the item instance
    3. Create a cart item instance
    4. Check if the cart item instance exists
    5. If it exists, increment the quantity
    6. If it doesn't exist, create a new cart item instance
    7. Create a cart instance
    8. Add the cart item to the cart instance
    9. Save the cart instance
    """
    user_instance = get_object_or_404(Customer, user=request.user)

    item_to_add = Item.objects.filter(id=id_unique).first()
    cart_item, created = CartItem.objects.get_or_create(item=item_to_add)

    if cart_item:
        cart_item.increment_quantity()
        cart_item.save()
        messages.info(request, 'Item quantity has been updated')
    else:
        messages.info(request, 'Sorry, there was a problem updating the item quantity')
        return redirect(reverse('shopping_cart:order_summary'))
    user_cart, created = Cart.objects.get_or_create(user=user_instance, ordered=False)
    user_cart.items.add(cart_item)
    user_cart.save()

    messages.info(request, "Item added to cart")
    return redirect(reverse('products:product-list'))



        

def remove_from_cart(request, unique_id):
    """
    1. Get the cart item instance
    2. Check if the cart item instance exists
    3. If it exists, delete the cart item instance
    4. If it doesn't exist, return an error message
    5. Redirect to the order summary page
    """
    item_to_delete = CartItem.objects.filter(pk=unique_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        messages.info(request, "Item has been deleted")
    return redirect(reverse('shopping_cart:order_summary'))
