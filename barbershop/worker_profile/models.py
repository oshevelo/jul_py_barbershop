from django.db import models
from apps_generic.whodidit.models import WhoDidIt, set_who_did_it


# Create your models here.


class WorkerProfile(WhoDidIt):
    """Profile for barbers and administrators"""

    first_name = models.CharField(max_length=15)
    second_name = models.CharField(max_length=15)
    position = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=18)
    email = models.CharField(max_length=50)
    worker = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.first_name


class WorkerCommunications(WhoDidIt):
    class Type:
        facebook_id = 'facebook_id'
        instagram_id = 'instagram_id'
        other_id = 'other_id'

    TYPES = [
        (Type.facebook_id, 'Facebook id'),
        (Type.instagram_id, 'Instagram id'),
        (Type.other_id, 'Other id'),
    ]

    social_network = models.CharField(
        max_length=50,
        choices=TYPES,
        blank=True, null=True
    )

    worker_profile = models.ForeignKey(WorkerProfile, on_delete=models.CASCADE)
    social_networks_ids = models.CharField(max_length=100)

    def __str__(self):
        return '{} Comm of type {} with id: {}'.format(self.worker_profile, self.type, self.social_networks_ids)
