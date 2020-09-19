from django.urls import path
from . import views

urlpatterns = [
    path('', views.CartDetails.as_view(), name='cart-details'),
    path('cartitem/', views.CartItemList.as_view(), name='cart-item-list'),
    path('cartitem/<int:cartitem_id>/', views.CartItemDetails.as_view(), name='cart-tem-details'),
]
