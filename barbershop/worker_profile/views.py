from django.shortcuts import render
from .models import WorkerProfile, WorkerCommunications
from .serializers import WorkerProfileSerializer, WorkerCommunicationsSerializer
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from worker_profile.permissions import WorkerPermission
from django.shortcuts import get_object_or_404
from rest_framework import filters


# Create your views here.


class WorkerProfileList(generics.ListCreateAPIView):
    queryset = WorkerProfile.objects.all()
    search_fields = ['first_name', 'second_name']
    filter_backends = (filters.SearchFilter,)
    serializer_class = WorkerProfileSerializer
    permission_classes = [WorkerPermission]
    pagination_class = LimitOffsetPagination

    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])


class WorkerProfileDetails(generics.RetrieveUpdateAPIView):
    serializer_class = WorkerProfileSerializer
    permission_classes = [WorkerPermission]

    def get_object(self):
        return get_object_or_404(WorkerProfile, pk=self.kwargs.get('worker_id'))


class WorkerCommunicationsList(generics.ListCreateAPIView):
    queryset = WorkerCommunications.objects.all()
    serializer_class = WorkerCommunicationsSerializer
    permission_classes = [WorkerPermission]
    pagination_class = LimitOffsetPagination


class WorkerCommunicationsDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkerCommunicationsSerializer
    permission_classes = [WorkerPermission]

    def get_object(self):
        return get_object_or_404(
            WorkerCommunications,
            worker_profile__worker=self.request.user,
            pk=self.kwargs.get('worker_profile_id')
        )
