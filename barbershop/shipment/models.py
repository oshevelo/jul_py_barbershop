from django.db import models


class Shipment(models.Model):
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
    user_name = models.CharField(max_length=20)
    user_surname = models.CharField(max_length=50)
    user_phone = models.CharField(max_length=15)
    user_email = models.CharField(max_length=30)
    user_address = models.CharField(max_length=30)
    user_comment = models.CharField(max_length=400)

