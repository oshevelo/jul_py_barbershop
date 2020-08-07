from django.db import models

# Create your models here.


class WorkerProfile(models.Model):
    """Profile for barbers and administrators"""
    first_name = models.CharField(max_length=15)
    second_name = models.CharField(max_length=15)
    position = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=18)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name

