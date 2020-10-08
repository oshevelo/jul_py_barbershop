from django.http import HttpResponse
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .serializers import ShipmentSerializer
from .models import Shipment
from rest_framework.pagination import LimitOffsetPagination


def index(request):
    return HttpResponse("Shipment")


class ShipmentList(generics.ListCreateAPIView):
    pagination_class = LimitOffsetPagination
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer()
    permission_classes = [IsAdminUser]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = ShipmentSerializer(queryset, many=True)
        return Response(serializer.data)


