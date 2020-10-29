from rest_framework import serializers
from .models import Catalog, Product


class CatalogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Catalog
        fields = ['name', 'slug']


class ProductSerializer(serializers.ModelSerializer):
    type = serializers.CharField(read_only= True)

    class Meta:
        model = Product
        fields = ['id', 'type', 'catalog', 'name', 'slug', 'price', 'stock', 'available',
                  'created_on',
                  'updated_on',
                  'created_by',
                  'updated_by'
                  ]

