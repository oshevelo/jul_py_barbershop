from rest_framework import generics
from .models import Catalog, Product
from django.shortcuts import get_object_or_404
from .serializers import CatalogSerializer, ProductSerializer
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly,BasePermission, SAFE_METHODS
from rest_framework import filters

from products.permissions import IsReadOnly, IsType_product_OrReadOnly_object


class CatalogList(generics.ListCreateAPIView):
    pagination_class = LimitOffsetPagination
    pagination_class.default_limit = 5
    pagination_class.max_limit = 15
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
    # permission_classes = [IsReadOnly]
    serializer_class = ProductSerializer
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)

    def get_queryset(self):
        print(self.request.GET)
        if self.request.GET.get('search'):
            return Product.objects.filter(name__istartswith=self.request.GET.get('search'))
        return Product.objects.all()


class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    pagination_class = LimitOffsetPagination
    # permission_classes = [IsAuthenticatedOrReadOnly, IsType_product_OrReadOnly_object]

    def get_object(self):
        return get_object_or_404(Product, pk=self.kwargs.get('product_id'))


