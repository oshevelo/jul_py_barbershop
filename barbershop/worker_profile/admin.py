from django.contrib import admin
from .models import WorkerProfile, WorkerCommunications


# Register your models here.


class WorkerProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        ('None', {'fields': ['first_name', 'second_name', 'position', 'phone_number', 'email']})
    ]
    list_display = ('first_name', 'second_name', 'position', 'phone_number', 'email', 'created_on', 'updated_by',)
    list_filter = ['position', 'created_on', 'updated_by']


admin.site.register(WorkerProfile, WorkerProfileAdmin)


class WorkerCommunicationsAdmin(admin.ModelAdmin):
    list_display = ('worker_profile', 'worker', 'type', 'created_on', 'updated_by')
    list_filter = ['created_on', 'updated_by']


admin.site.register(WorkerCommunications, WorkerCommunicationsAdmin)