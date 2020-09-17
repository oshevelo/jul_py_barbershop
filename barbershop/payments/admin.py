from django.contrib import admin
from .models import Payment


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id',
                    #               'order',
                    'bill_amount',
                    'type',
                    'status',
                    'payee_name',
                    'payee_surname',
                    'payee_email',
                    'user',
                    'created_on',
                    'updated_on',
                    'created_by',
                    'updated_by',
                    )


admin.site.register(Payment, PaymentAdmin)
