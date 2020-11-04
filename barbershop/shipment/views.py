from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .serializers import ShipmentSerializer
from .models import Shipment
from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import get_object_or_404


class ShipmentList(generics.ListCreateAPIView):
    pagination_class = LimitOffsetPagination
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        print(self.request.GET)
        return Shipment.objects.filter(name__istartswith=self.request.GET.get('search'))


class ShipmentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer

    def get_object(self):
        return get_object_or_404(Shipment, pk=self.kwargs.get('shipment_id'))

