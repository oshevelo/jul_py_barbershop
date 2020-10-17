import datetime
from django.db import models
from apps_generic.whodidit.models import WhoDidIt, set_who_did_it
from django.utils import timezone


class Catalog(models.Model):
    name = models.CharField('Catalog', max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Catalog'
        verbose_name_plural = 'Cataloges'

    def __str__(self):
        return self.name


class Product(WhoDidIt):
    """products and prices"""
    class Type:
        hair_cut = 'hair_cut'
        product = 'product'

    TYPES = [
        (Type.hair_cut, 'Hair Cut'),
        (Type.product, 'Product'),
    ]
    type = models.CharField(
        max_length=50,
        choices=TYPES,
        default=Type.product,
    )
    catalog = models.ForeignKey(Catalog,  on_delete=models.CASCADE)
    name = models.CharField("Product", max_length=200)
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
