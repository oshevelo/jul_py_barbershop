from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventDetails.as_view(), name='event-details'),
    path('event/', views.EventList.as_view(), name='event-list'),
    path('event/<int:event_id>/', views.EventDetails.as_view(), name='event-list')
]