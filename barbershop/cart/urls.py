from django.urls import path

from . import views

urlpatterns = [
    path('', views.CartDetail.as_view(), name='index'),
    path('cartitem/', views.CartItemList.as_view(), name='list'),
    path('cartitem/<int:cartitem_id>/', views.CartItemDetail.as_view(), name='details'),
]
