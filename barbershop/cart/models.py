from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from apps_generic.whodidit.models import WhoDidIt

# Create your models here.


class Cart(WhoDidIt):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    pub_date = models.DateTimeField('date published')

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    #TODO made correct __str__

    # def __str__(self):
    #     return self.Meta.verbose_name


class CartItem(WhoDidIt):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sum = models.IntegerField()
    count = models.PositiveSmallIntegerField(default=1)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    # TODO made correct __str__

    # def __str__(self):
    #     return self.Meta.verbose_name
