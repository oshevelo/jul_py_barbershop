from django.db import models
from apps_generic.whodidit.models import WhoDidIt


class Shipment(WhoDidIt):
    """methods of shipment"""

    class ShipmentType:
        pick_up = 'pick up'
        novaposhta = 'nova poshta'

    TYPES = [
        (ShipmentType.pick_up, 'Pick up'),
        (ShipmentType.novaposhta, 'Nova Poshta')
    ]

    type = models.CharField(
        max_length=40,
        choices=TYPES,
        default=ShipmentType.novaposhta,
    )

    class ShipmentStatus:
        collected = 'collected'
        in_transit = 'in transit'
        arrived_at_destination = 'arrived at destination'
        delivered = 'delivered'

    STATUS = [
        (ShipmentStatus.collected, 'Collected'),
        (ShipmentStatus.in_transit, 'In transit'),
        (ShipmentStatus.arrived_at_destination, 'Arrived at destination'),
        (ShipmentStatus.delivered, 'Delivered')
    ]

    status = models.CharField(
        max_length=40,
        choices=STATUS,
        default=ShipmentStatus.collected,
    )

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    shipment_id = models.CharField(max_length=50)
    buyer_name = models.CharField(max_length=50)
    buyer_surname = models.CharField(max_length=50)
    buyer_phone = models.CharField(max_length=15)
    buyer_email = models.CharField(max_length=30)
    buyer_address = models.CharField(max_length=30)
    buyer_comment = models.CharField(max_length=400, blank=True)
