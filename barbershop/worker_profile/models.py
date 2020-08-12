from django.db import models

# Create your models here.


class WorkerProfile(models.Model):
    """Profile for barbers and administrators"""
    first_name = models.CharField(max_length=15)
    second_name = models.CharField(max_length=15)
    position = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=18)
    email = models.CharField(max_length=50)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name


class WorkerCommunications(models.Model):
    """Extra communications for workers"""
    social_networks = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    facebook = models.CharField(max_length=40)
    instagram = models.CharField(max_length=40)

    def __str__(self):
        return self.social_networks

