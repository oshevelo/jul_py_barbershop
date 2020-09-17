from rest_framework import generics
from .models import Catalog, Product
from django.shortcuts import get_object_or_404
from .serializers import CatalogSerializer, ProductSerializer
from rest_framework.pagination import LimitOffsetPagination


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
#    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        print(self.request.GET)
        if self.request.GET.get('search'):
            return Product.objects.filter(name__istartswith=self.request.GET.get('search'))
        return Product.objects.all()


class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Catalog.objects.all()
    serializer_class = ProductSerializer

    def get_object(self):
        return get_object_or_404(Product, pk=self.kwargs.get('product_id'))


