# # from rest_framework.permissions import BasePermission, SAFE_METHODS
# from rest_framework import generics
# from .models import Catalog, Product
# from django.shortcuts import get_object_or_404
# from .serializers import CatalogSerializer, ProductSerializer
# from rest_framework.pagination import LimitOffsetPagination
# from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
#
#
# class CatalogList(generics.ListCreateAPIView):
#     queryset = Catalog.objects.all()
#     serializer_class = CatalogSerializer
#
#
# class CatalogDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Catalog.objects.all()
#     serializer_class = CatalogSerializer
#
#     def get_object(self):
#         return get_object_or_404(Catalog, pk=self.kwargs.get('catalog_id'))
#
#
# class ProductListPermission(generics.ListCreateAPIView):
#     pagination_class = LimitOffsetPagination
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     pagination_class.default_limit = 5
#     pagination_class.max_limit = 15
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
# class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Catalog.objects.all()
#     serializer_class = ProductSerializer
#
#     def get_object(self):
#         return get_object_or_404(Product, pk=self.kwargs.get('product_id'))
#
# class IsOwnerOrReadOnly(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.method in SAFE_METHODS:
#             return True
#         return obj.Product.
#             # obj.cart.user == request.user
# '''
# class CartPermissions(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return get_object_or_404(Cart, pk=view.kwargs.get('cart_id'),
#                                 user=view.request.user,
#                                 )
#
# class CartItemPermissions(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return get_object_or_404(CartItem, pk=view.kwargs.get('cartitem_id'),
#                                 user=view.request.user,
#                                 )
# '''
# class AddCartItemPermission(BasePermission):
#     def has_permission(self, request, view):
#         if request.method == 'POST':
#             cartitem = get_object_or_404(CartItem,
#                                      # pk=view.kwargs.get('cartitem_id'),
#                                      user=view.request.user,
#                                      )
#             return cartitem
