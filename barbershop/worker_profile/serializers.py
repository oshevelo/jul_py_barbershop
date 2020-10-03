from .models import WorkerProfile, WorkerCommunications
from rest_framework import serializers


class WorkerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerProfile
        fields = ['id', 'first_name', 'second_name', 'position', 'phone_number', 'email', 'worker']


class WorkerCommunicationsSerializer(serializers.ModelSerializer):
    social_network = serializers.CharField(source='get_type_display')

    class Meta:
        model = WorkerCommunications
        fields = ['id', 'worker_profile_id', 'social_network', 'social_networks_ids']
