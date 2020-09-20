from rest_framework import serializers
from .models import Order, OrderItem
from blog.serializers import UserSerializer
from cart.serializers import CartInOrderSerializer
from cart.models import Cart, CartItem
from random import randint


class OrderSerializer(serializers.ModelSerializer): 
    client = UserSerializer(read_only=True)
    order_sum = serializers.DecimalField(max_digits = 5, decimal_places = 2, read_only=True)
    cart = CartInOrderSerializer()
    order_id = serializers.CharField(read_only=True) 
    

    def validate(self, *args, **kwargs):
        cart_id = args[0]['cart']['id']
        cart = Cart.objects.get(id=cart_id)

        if cart.user != self.context['request'].user:
            raise serializers.ValidationError('Don`t owner')

        print(self.context['request'].user)
        
        
        return super().validate(*args, **kwargs)

    def create(self, validated_data):
        cart_id = validated_data['cart']['id']
        cart = Cart.objects.get(id=cart_id)
        order = Order.objects.create(
            client=cart.user,
            cart=cart,
            order_sum=0,
            order_id=randint(0, 200000)
        )                
        for cart_item in cart.cart_items.all():
            order_item = OrderItem.objects.create(
                order = order,
                product = cart_item.product,
                sum = cart_item.sum,
                count = cart_item.count
            )

            print(cart_item)


        #{'cart': OrderedDict([('id', 1)])}
        #print(validated_data, cart_id, dir(cart))
        return order

    class Meta:
        model = Order
        fields = [
            'client',
            'cart',
            'order_sum',
            'order_id'
        ]


