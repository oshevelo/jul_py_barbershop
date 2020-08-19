import datetime

from django.db import models
from django.utils import timezone


class Catalog(models.Model):
    name = models.CharField('Catalog',max_length=200)
    slug = models.SlugField(max_length=200,  unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Catalog'
        verbose_name_plural = 'Cataloges'

    def __str__(self):
        return self.name


class Product(models.Model):
    """products and prices"""
    cataloge = models.ForeignKey(Catalog,  on_delete=models.CASCADE)
    name = models.CharField("Products", max_length=200)
    slug = models.SlugField(max_length=200, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name


class Haircut(models.Model):
    """Haircuts and prices"""
    name = models.CharField("Haircut", max_length=100, )
    prices = models.PositiveIntegerField("Prices", default=0, help_text="indicate the cost")
    description = models.TextField("Description")

    class Meta:
        verbose_name = 'Haircut'
        verbose_name_plural = 'Haircuts'

    def __str__(self):
        return self.name
