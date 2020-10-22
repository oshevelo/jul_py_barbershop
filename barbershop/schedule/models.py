from django.db import models
from apps_generic.whodidit.models import WhoDidIt, set_who_did_it
from django.contrib.auth.models import User
from worker_profile.models import WorkerProfile
#from products.models import Product


class Event(models.Model):

    class Type:
        reservation = 'reservation'
        shift = 'shift'

    TYPES = [
        (Type.reservation, 'Reservation'),
        (Type.shift, 'Shift')
    ]

    class Status:
        scheduled = 'scheduled'
        canceled = 'canceled'
        finished = 'finished'

    STATUS = [
        (Status.scheduled, 'Scheduled'),
        (Status.canceled, 'Canceled'),
        (Status.finished, 'Finished'),
    ]

    type = models.CharField(
        max_length=50,
        choices=TYPES,
        default=Type.reservation,
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS,
        default=Status.scheduled
    )
    client = models.ForeignKey(User, on_delete=models.CASCADE, default=None, verbose_name='Client', related_name='client', blank=True)
    #barber = models.ForeignKey(WorkerProfile, on_delete=models.CASCADE, default=None, verbose_name='Barber', related_name='barber')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return 'Event type:{} start:{} end {}'.format(self.type, self.start_time, self.end_time)

    def cancel(self):
        self.status = self.Status.canceled

    def finish(self):
        self.status = self.Status.finished


