from django.urls import path, include
from . import views


urlpatterns = [
    path('catalog/', views.CatalogList.as_view(), name='list'),
    path('catalog/<int:catalog_id>/', views.CatalogDetails.as_view(), name='details'),
    path('products/', views.ProductList.as_view(), name='list'),
    path('products/<int:products_id>/', views.ProductDetails.as_view(), name='details'),
]
