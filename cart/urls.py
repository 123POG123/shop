from .views import cart_detail, cart_remove, cart_add
from django.urls import path

urlpatterns = [
    path('cart/', cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', cart_add, name='cart_add'),
    path('remove/<int:product_id>/', cart_remove, name='cart_remove'),
]
