from rest_framework import generics
from .models import Catalog, Product
from django.shortcuts import get_object_or_404
from .serializers import CatalogSerializer, ProductSerializer
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class CatalogList(generics.ListCreateAPIView):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer


class CatalogDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer

    def get_object(self):
        return get_object_or_404(Catalog, pk=self.kwargs.get('catalog_id'))


class ProductList(generics.ListCreateAPIView):
    pagination_class = LimitOffsetPagination
    pagination_class.default_limit = 5
    pagination_class.max_limit = 15
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ProductSerializer


class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Catalog.objects.all()
    serializer_class = ProductSerializer


    def get_object(self):
        return get_object_or_404(Product, pk=self.kwargs.get('product_id'))


