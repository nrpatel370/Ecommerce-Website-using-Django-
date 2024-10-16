from rest_framework import serializers
from .models import Product, Collection, Review
from decimal import Decimal

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'product_count']
    # id = serializers.IntegerField()
    # title = serializers.CharField()
    product_count = serializers.IntegerField(read_only = True)
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title','description', 'unit_price', 'slug', 'inventory','price_with_tax','collection']
    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length = 255)
    # unit_price = serializers.DecimalField(max_digits = 6, decimal_places = 2)
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    # collection = serializers.HyperlinkedRelatedField(queryset = Collection.objects.all(), view_name='collection-detail')

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)
    
    # def create(self, validated_data):
    #     product = Product(**validated_data)
    #     product.other = 1
    #     product.save()
    #     return product

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields= ['id', 'date', 'name', 'description']
    
    def create(self, validated_data):
        product_id = self.context['product_id']
        return Review.objects.create(product_id=product_id, **validated_data)