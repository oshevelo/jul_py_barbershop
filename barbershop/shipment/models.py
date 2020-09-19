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

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    buyer_name = models.CharField(max_length=20)
    buyer_surname = models.CharField(max_length=50)
    buyer_phone = models.CharField(max_length=15)
    buyer_email = models.CharField(max_length=30)
    buyer_address = models.CharField(max_length=30)
    buyer_comment = models.CharField(max_length=400, blank=True)
