from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework import generics
from .models import Catalog, Product
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class FirstPermissin(BasePermission):
    """
    Permission for:
        -> Authenticated: read_only and create
        -> Owner: update and delete
        -> Anonimus: read_only
    """


    def has_permission(self, request, view):

