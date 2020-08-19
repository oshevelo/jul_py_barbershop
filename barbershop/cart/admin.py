from django.contrib import admin
from .models import Cart, CartItem

# Register your models here.

class CartAdmindmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'pub_date')


admin.site.register(Cart, CartAdmindmin)

class CartItemAdmindmin(admin.ModelAdmin):
    pass

admin.site.register(CartItem, CartItemAdmindmin)
