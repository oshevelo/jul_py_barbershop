import datetime

from django.db import models
from django.utils import timezone


class Products(models.Model):
    """products and prices"""
    name = models.CharField("Products", max_length=100)
    prices = models.PositiveIntegerField("Prices", default=0, help_text="indicate the cost")
    description = models.TextField("Description")
    # image = models.ImageField("Image", upload_to="Gallery/")

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

