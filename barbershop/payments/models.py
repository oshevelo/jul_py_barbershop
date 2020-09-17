from django.db import models
from apps_generic.whodidit.models import WhoDidIt


class Payment(WhoDidIt):
    # order = models.ForeignKey('orders.Order', on_delete=models.PROTECT, null=True, blank=False)
    bill_amount = models.DecimalField(max_digits=10, decimal_places=2)

    class PaymentType:
        cash = 'cash'
        portmone = 'portmone'

    TYPE = [
        (PaymentType.cash, 'cash'),
        (PaymentType.portmone, 'Portmone'),
    ]

    type = models.CharField(
        max_length=20,
        choices=TYPE,
        default=PaymentType.cash,
    )

    class PaymentStatus:
        waiting = 'waiting'
        input = 'input'
        preauth = 'preauth'
        confirmed = 'confirmed'
        rejected = 'rejected'
        refunded = 'refunded'
        error = 'error'

    STATUS = [
        (PaymentStatus.waiting, 'waiting'),
        (PaymentStatus.input, 'input'),
        (PaymentStatus.preauth, 'preauth'),
        (PaymentStatus.confirmed, 'confirmed'),
        (PaymentStatus.rejected, 'rejected'),
        (PaymentStatus.refunded, 'refunded'),
        (PaymentStatus.error, 'error'),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default=PaymentStatus.waiting,
    )

    payee_name = models.CharField(max_length=50)
    payee_surname = models.CharField(max_length=50)
    payee_email = models.CharField(max_length=50)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'

    # def __str__(self):
    #    return 'payment for order {} by {} is {}'.format(self.order, self.user, self.status)


class PaymentSystemLog(models.Model):
    # request
    # shop_order_number = models.ForeignKey('orders.Order', on_delete=models.PROTECT, null=True, blank=False)
    payee_id = models.IntegerField(null=True, blank=False)
    dt = models.DateTimeField(auto_now=True)
    bill_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=False)
    # response
    SHOPBILLID = models.IntegerField(null=True, blank=False)
    SHOPORDERNUMBER = models.CharField(max_length=100, null=True, blank=False)
    BILL_AMOUNT = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=False)
    RESULT = models.IntegerField(null=True, blank=False)

    # def __str__(self):
    #    return 'order {} by {} is {}'.format(self.shop_order_number, self.payee_id, self.RESULT)
