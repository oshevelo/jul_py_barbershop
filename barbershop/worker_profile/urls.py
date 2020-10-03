from django.urls import path

from . import views

urlpatterns = [
    path('worker_profile/', views.WorkerProfileList.as_view(), name='list'),
    path('worker_profile/<int:worker_id>/', views.WorkerProfileDetails.as_view(), name='details'),
    path('worker_profile/worker_communications/', views.WorkerCommunicationsList.as_view(), name='list'),
    path('worker_profile/worker_communications/<int:worker_profile_id>/', views.WorkerCommunicationsDetails.as_view(), name='details'),
]