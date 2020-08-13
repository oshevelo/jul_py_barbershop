from django.db import models
#from cart.models import Order


class Payment(models.Model):
    #amount = models.OneToOneField(Order, on_delete=models.CASCADE)
    description = models.CharField(max_length=128, blank=True)
    buyer = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return 'Payment {} is {}'.format(self.id, self.paid)
    
        
        
