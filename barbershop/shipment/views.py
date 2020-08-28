from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Shipment
from .serializers import ShipmentSerializer


def index(request):
    return HttpResponse("Shipment")


@api_view(['GET'])
def shipment_details_view(request):

    try:
        shipment = Shipment.objects.get()
    except Shipment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ShipmentSerializer(shipment)
        return Response(serializer.data)
