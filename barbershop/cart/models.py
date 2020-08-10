from django.db import models

# Create your models here.
class Cart(models.Model):
    # TODO Wait products app
    # cart_product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    cart_count = models.PositiveSmallIntegerField(default=1)
    cart_pub_date = models.DateTimeField('date published')