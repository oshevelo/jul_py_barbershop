from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from apps_generic.whodidit.models import WhoDidIt


class Cart(WhoDidIt):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, verbose_name='User')
    pub_date = models.DateTimeField('Date of publication')

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    def __str__(self):
        return 'Cart'

class CartItem(WhoDidIt):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Item name')
    sum = models.FloatField(verbose_name='Sum')
    count = models.PositiveSmallIntegerField(default=1, verbose_name='Amount')

    class Meta:
        verbose_name = 'Cart item'
        verbose_name_plural = 'Cart items'

    def __str__(self):
        return 'Cart item'
