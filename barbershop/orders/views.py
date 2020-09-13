from rest_framework import generics
from .models import Order
from django.shortcuts import get_object_or_404
from .serializers import OrderSerializer
from rest_framework.pagination import LimitOffsetPagination

class OrdersList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = LimitOffsetPagination

class OrdersDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer

    def get_object(self):
        return get_object_or_404(Order, order_id=self.kwargs.get('order_id'))

