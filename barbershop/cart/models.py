from django.db import models

# Create your models here.
class Cart(models.Model):
    # TODO Wait products app
    user = models.ForeignKey(User, )
    cart_pub_date = models.DateTimeField('date published')

class CartItem(models.Model):
