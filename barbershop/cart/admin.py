from django.contrib import admin
from .models import Cart

# Register your models here.

class CartAdmindmin(admin.ModelAdmin):
    fieldsets = [
        ('None', {'fields': ['cart_count', 'cart_pub_date']})
    ]
    list_display = ('cart_count', 'cart_pub_date')


admin.site.register(Cart, CartAdmindmin)