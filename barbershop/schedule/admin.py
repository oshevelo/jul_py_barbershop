from django.contrib import admin
from .models import Event

#from django.contrib.contenttypes.admin import GenericStackedInline


class EventAdmin(admin.ModelAdmin):
    list_display = ['client', 'start_time', 'end_time']


admin.site.register(Event, EventAdmin)