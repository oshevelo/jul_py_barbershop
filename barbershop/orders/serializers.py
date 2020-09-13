from rest_framework import serializers
from .models import Order
from blog.serializers import UserSerializer
from cart.serializers import CartDetailSerializer


class OrderSerializer(serializers.ModelSerializer):
    client = UserSerializer()
    cart = CartDetailSerializer()
    class Meta:
        model = Order
        fields = [
            'client',
            'cart',
            'order_sum',
            'order_id'
        ]
