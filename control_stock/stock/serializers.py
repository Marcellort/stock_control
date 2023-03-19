from rest_framework import serializers


from .models import Product, Sale


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class SaleCreateSerializer(serializers.ModelSerializer):
    profit = serializers.HiddenField(default=0.0)
    class Meta:
        model = Sale
        fields = ['product','sell_price','quantity_sale','profit']


class SaleSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False)
    class Meta:
        model = Sale
        fields = '__all__'