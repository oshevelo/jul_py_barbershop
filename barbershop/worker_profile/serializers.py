from .models import WorkerProfile, WorkerCommunications
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email'
        ]


class WorkerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerProfile
        fields = ['id', 'first_name', 'second_name', 'position', 'phone_number', 'email', 'worker']


class WorkerCommunicationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkerCommunications
        fields = ['id', 'worker_profile',  'social_network', 'social_networks_ids']
