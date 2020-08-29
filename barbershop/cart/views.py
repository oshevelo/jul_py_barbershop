from .serializers import CartSerializer, CartItemSerializer
from .models import Cart, CartItem
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

class CartList(viewsets.ModelViewSet):
    pagination_class = LimitOffsetPagination
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartItemList(viewsets.ModelViewSet):
    pagination_class = LimitOffsetPagination
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer