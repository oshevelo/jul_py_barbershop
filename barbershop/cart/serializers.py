from .models import Cart, CartItem
from rest_framework import serializers


class CartDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'user', 'pub_date']        

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'cart_id', 'product_id', 'sum', 'count']

class CartItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'cart_id', 'product_id', 'sum', 'count']

class CartInOrderSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()    
    class Meta:
        model = Cart
        fields = ['id'] 

