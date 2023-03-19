from django.db import models
import uuid

class Product(models.Model):
    id = models.UUIDField(primary_key=True,unique=True,editable=False,default=uuid.uuid4)
    name = models.TextField()
    color = models.CharField(max_length=50)
    stock_quantity = models.IntegerField(blank=False,null=False)
    buy_price = models.DecimalField(blank=False,null=False, max_digits=10,decimal_places=2)

    def __str__(self) -> str:
        return f"id={self.id}, name={self.name},color={self.color},stock_quantity={self.stock_quantity}, buy_price{self.buy_price}"

class Sale(models.Model):
    id = models.UUIDField(primary_key=True,unique=True,editable=False,default=uuid.uuid4)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sell_price = models.DecimalField(blank=False,null=False, max_digits=10,decimal_places=2)
    quantity_sale = models.IntegerField(blank=False,null=False)
    profit = models.DecimalField(blank=False,null=False, max_digits=10,decimal_places=2)