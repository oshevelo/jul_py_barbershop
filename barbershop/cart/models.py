from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from apps_generic.whodidit.models import WhoDidIt

# Create your models here.


class Cart(WhoDidIt):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, verbose_name='Пользователь')
    pub_date = models.DateTimeField('Дата публикации')

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return 'Корзина'

class CartItem(WhoDidIt):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Имя товара')
    sum = models.FloatField(verbose_name='Сумма')
    count = models.PositiveSmallIntegerField(default=1, verbose_name='Количество')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return 'Товар корзины'
