from django.db import models
from django.contrib.auth.models import User
from barbershop.products.models import Products

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_pub_date = models.DateTimeField('date published')

class CartItem(models.Model):
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    sum = models.IntegerField()
    count = models.PositiveSmallIntegerField(default=1)