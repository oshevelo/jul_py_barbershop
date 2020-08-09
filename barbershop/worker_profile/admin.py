from django.contrib import admin
from .models import WorkerProfile

# Register your models here.


class WorkerProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        ('None', {'fields': ['first_name', 'second_name', 'position', 'phone_number', 'email']})
    ]
    list_display = ('first_name', 'second_name', 'position', 'phone_number', 'email')


admin.site.register(WorkerProfile, WorkerProfileAdmin)