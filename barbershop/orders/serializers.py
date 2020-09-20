from rest_framework import serializers
from .models import Order
from blog.serializers import UserSerializer
from cart.serializers import CartInOrderSerializer
from cart.models import Cart
from random import randint


class OrderSerializer(serializers.ModelSerializer): 
    client = UserSerializer(read_only=True)
    order_sum = serializers.DecimalField(max_digits = 5, decimal_places = 2, read_only=True)
    cart = CartInOrderSerializer()
    order_id = serializers.CharField(read_only=True) 
    

    def create(self, validated_data):
        cart_id = validated_data['cart']['id']
        cart = Cart.objects.get(id=cart_id)
        order = Order.objects.create(
            client=cart.user,
            cart=cart,
            order_sum=0,
            order_id=randint(0, 200000)
        )                
        #{'cart': OrderedDict([('id', 1)])}
        print(validated_data, cart_id)
        return order

    class Meta:
        model = Order
        fields = [
            'client',
            'cart',
            'order_sum',
            'order_id'
        ]


