from django.urls import path

from . import views

urlpatterns = [
    path('', views.WorkerProfileList.as_view(), name='list'),
    path('worker_profile/<int:worker_profile_id>/', views.WorkerProfileDetails.as_view(), name='details'),
    path('', views.WorkerCommunicationsList.as_view(), name='list'),
    path('worker_communications/<int:worker_communications_id>/', views.WorkerCommunicationsDetails.as_view(), name='details'),
]