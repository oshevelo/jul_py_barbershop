from django.db import models


class Shipment(models.Model):
    method = models.CharField(max_length=30, default="novaposhta")
    description = models.CharField(max_length=100)
    #cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    buyer = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.method

