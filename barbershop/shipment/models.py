from django.db import models


class Shipment(models.Model):
    description = models.CharField(max_length=128, blank=True)
    cart = models.ForeignKey('user.cart', on_delete=models.CASCADE)
    buyer = models.ForeignKey('auth.User', on_delete=models.CASCADE)
