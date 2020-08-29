from django.contrib import admin
from .models import Cart, CartItem


class CartItemAdmin(admin.StackedInline):
    model = CartItem

class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemAdmin]
    list_display = ('user', 'pub_date')

admin.site.register(Cart, CartAdmin)