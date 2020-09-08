from .models import WorkerProfile, WorkerCommunications
from rest_framework import serializers


class WorkerProfileSerializer(serializers.Serializer):
    class Meta:
        model = WorkerProfile
        fields = ['first_name', 'second_name', 'position', 'phone_number', 'email', 'worker']


class WorkerCommunicationsSerializer(serializers.Serializer):
    class Meta:
        model = WorkerCommunications
        fields = '__all__'
