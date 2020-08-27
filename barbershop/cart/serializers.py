# from .models import Cart, CartItem
# from rest_framework import serializers
#
# class CartSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Cart
#         fields = ['id', 'user', 'cart_pub_date']
#
# class CartDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Cart
#         fields = ['id', 'user', 'cart_pub_date']
#
# class CartItemDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CartItem
#         fields = ['id', 'cart_id', 'product_id', 'sum', 'count']
#
# class CartItemDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CartItem
#         fields = ['id', 'cart_id', 'product_id', 'sum', 'count']
