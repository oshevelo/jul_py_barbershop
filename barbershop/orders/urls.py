from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrdersList.as_view(), name='list'),
    path('<str:order_id>/', views.OrdersDetails.as_view(), name='details'),
]
