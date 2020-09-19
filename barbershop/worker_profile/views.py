from django.shortcuts import render
from worker_profile.models import WorkerProfile, WorkerCommunications
from worker_profile.serializers import WorkerProfileSerializer, WorkerCommunicationsSerializer
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_object_or_404


# Create your views here.


class WorkerProfileList(generics.ListCreateAPIView):
    queryset = WorkerProfile.objects.all()
    serializer_class = WorkerProfileSerializer
    permission_classes = [IsAdminUser]
    pagination_class = LimitOffsetPagination


class WorkerProfileDetails(generics.RetrieveUpdateAPIView):
    serializer_class = WorkerProfileSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        worker = get_object_or_404(WorkerProfile.worker, pk=self.kwargs.get('worker_id'))
        return worker


class WorkerCommunicationsList(generics.ListCreateAPIView):
    queryset = WorkerCommunications.objects.all()
    serializer_class = WorkerCommunicationsSerializer
    permission_classes = [IsAdminUser]
    pagination_class = LimitOffsetPagination


class WorkerCommunicationsDetails(generics.RetrieveUpdateAPIView):
    serializer_class = WorkerCommunicationsSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        worker_profile = get_object_or_404(WorkerCommunications.worker_profile, pk=self.kwargs.get('worker_profile_id'))
        return worker_profile
