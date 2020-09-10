from rest_framework import serializers
from .models import Shipment


class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = ['user', 'buyer_name', 'buyer_surname', 'buyer_phone', 'buyer_email', 'buyer_address',
                  'buyer_comment']
