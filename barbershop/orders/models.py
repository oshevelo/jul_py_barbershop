from django.db import models
from apps_generic.whodidit.models import WhoDidIt, set_who_did_it


class Order(WhoDidIt):
    client = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True)
    cart = models.OneToOneField('cart.Cart', on_delete=models.CASCADE,)
    order_sum = models.DecimalField(max_digits=10, decimal_places=2)
    order_id = models.CharField("Order", max_length=100)

    class Meta:
        ordering = ('order_id',)
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return '{} {} price {}'.format(self.client, self.order_id, self.order_sum)

