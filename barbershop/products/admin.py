from django.contrib import admin
from .models import Products


class ProductsAdmin(admin.ModelAdmin):
    fieldsets = [
        ("None", {'fields': ['name', 'prices', 'description']})
    ]
    list_display = ('name', 'prices', 'description')


admin.site.register(Products, ProductsAdmin)
