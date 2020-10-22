from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .serializers import EventDetailsSerializer
from .models import Event


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventDetailsSerializer
    #pagination_class = StandartPagination


class EventDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventDetailsSerializer
    #pagination_class = LimitOffsetPagination
    #permission_classes = [IsAuthenticated]

    def get_object(self):
        event = get_object_or_404(Event)
        return event

