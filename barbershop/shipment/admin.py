from django.contrib import admin
from .models import Shipment

admin.site.register(Shipment, admin.ModelAdmin)


# Register your models here.
