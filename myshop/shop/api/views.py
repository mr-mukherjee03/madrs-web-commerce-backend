
from rest_framework import generics,viewsets
from shop.api.serializers import CategorySerializer, ProductSerializer
from shop.models import Category,Product
from shop.api.pagination import StandardPagination
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

"""class CategoryListView(generics.ListAPIView):
    queryset=Category.objects.annotate(total_products=Count('products'))
    serializer_class=CategorySerializer
    pagination_class=StandardPagination


class CategoryDetailView(generics.RetrieveAPIView):
    queryset=Category.objects.annotate(total_products=Count('products'))
    serializer_class=CategorySerializer
"""


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=Category.objects.prefetch_related('product')
    serializer_class=CategorySerializer
    pagination_class=StandardPagination

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    pagination_class=StandardPagination

