

from rest_framework import serializers
from shop.models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    total_products=serializers.IntegerField()
    class Meta:
        model=Category
        fields=['id','name','slug']

    
class ProductSerializer(serializers.ModelSerializer):
    category=CategorySerializer(many=True, read_only=True)

    class Meta:
        model=Product
