from django.contrib import admin
from .models import Haircut, Catalog, Product


class HaircutAdmin(admin.ModelAdmin):
    fieldsets = [
        ("None", {'fields': ['name', 'prices', 'description']})
    ]
    list_display = ('name', 'prices', 'description')


admin.site.register(Haircut, HaircutAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Catalog, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price', 'stock', 'available', 'created', 'updated')
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
