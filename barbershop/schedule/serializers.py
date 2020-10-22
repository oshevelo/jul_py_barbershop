from rest_framework import serializers
from .models import Event


class EventDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'type', 'client', 'start_time', 'end_time', 'status', ]



