from django.urls import path
from . import views


urlpatterns = [
    path('add-to-cart/<int:id_unique>/', views.add_to_cart, name='add_to_cart'),
]