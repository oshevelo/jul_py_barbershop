from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'carts', views.CartList)
router.register(r'cart-items', views.CartItemList)
urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
]