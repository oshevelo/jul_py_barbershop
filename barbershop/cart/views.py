from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from cart.serializers import CartDetailSerializer, CartItemSerializer, CartItemDetailSerializer
from cart.models import Cart, CartItem
from rest_framework.pagination import LimitOffsetPagination
from cart.permissions import IsOwnerOrReadOnly


class CartDetails(generics.RetrieveAPIView):
    serializer_class = CartDetailSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticated]

    def get_object(self):
        cart = get_object_or_404(Cart, user=self.request.user)
        return cart

class CartItemList(generics.ListCreateAPIView):
    serializer_class = CartItemSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        cart = get_object_or_404(Cart, user=self.request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        return cart_items

class CartItemDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemDetailSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_object(self):
        cart_item = get_object_or_404(CartItem, pk=self.kwargs.get('cartitem_id'))
        return cart_item