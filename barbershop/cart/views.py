from django.http import HttpResponse
from django.http import Http404
from cart.models import Cart, CartItem
from rest_framework.permissions import IsAuthenticated

from rest_framework import generics
from cart.serializers import CartSerializer, CartItemDetailSerializer
from cart.permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404


class CartDetail(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]#IsOwnerOrReadOnly, CartPermissions, ]

    def get_object(self):
        cart = get_object_or_404(Cart, user=self.request.user)
        return cart


class CartItemList(generics.ListCreateAPIView):
    
    serializer_class = CartItemDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        cart = get_object_or_404(Cart, user=self.request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        return cart_items


class CartItemDetail(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = CartItemDetailSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_object(self):
        cart = get_object_or_404(CartItem, pk=self.kwargs.get('cartitem_id'))
        return cart
