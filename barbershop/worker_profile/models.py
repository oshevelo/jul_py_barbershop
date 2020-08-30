from django.db import models


# Create your models here.


class WorkerProfile(models.Model):
    """Profile for barbers and administrators"""

    class Type:
        facebook_id = 'Facebook id'
        instagram_id = 'Instagram id'
        other_id = 'Other id'

    TYPES = [
        (Type.facebook_id, 'Facebook id'),
        (Type.instagram_id, 'Instagram id'),
        (Type.other_id, 'Other id'),
    ]

    type = models.CharField(
        max_length=50,
        choices=TYPES,
        default=None,
    )

    first_name = models.CharField(max_length=15)
    second_name = models.CharField(max_length=15)
    position = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=18)
    email = models.CharField(max_length=50)
    worker = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.first_name
