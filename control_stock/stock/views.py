from .models import Product, Sale
from .serializers import ProductSerializer, SaleSerializer, SaleCreateSerializer
from rest_framework import viewsets
from decimal import Decimal

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST" or self.request.method == "PATH":
            return SaleCreateSerializer
        return SaleSerializer

    def create(self, request, *args, **kwargs):
        setattr(request.data, '_mutable', True)
        product_sale = Product.objects.get(id=request.data['product'])
        if product_sale.stock_quantity > 0:
            product_sale.stock_quantity -=int(request.data['quantity_sale'])
        product_sale.save()
        request.data['profit'] = str(Decimal(request.data['sell_price']) - product_sale.buy_price)
        breakpoint()
        return super().create(request, *args, **kwargs)