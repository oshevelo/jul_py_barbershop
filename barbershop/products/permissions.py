from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework import generics
from .models import Catalog, Product
from django.shortcuts import get_object_or_404
from .serializers import CatalogSerializer, ProductSerializer
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class IsOwnerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request == view


class IsOwnerOrReadOnly_object(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.type == Product.Type.product

