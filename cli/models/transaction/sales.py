from models.database import BaseModel
from peewee import *
from models.people.clients import Client
from models.transaction.payments import PaymentMethod
from models.catalog.products import Product
from datetime import datetime  # Para usar datetime.now()

class Sale(BaseModel):
    sale_id = AutoField(primary_key=True)
    date_of_purchase = DateTimeField(null=False, default=datetime.now)
    client = ForeignKeyField(Client, field='client_id', null=True)
    total = DecimalField(max_digits=10, decimal_places=2, null=False)
    payment_method = ForeignKeyField(PaymentMethod, field='payment_method_id', null=True)

class SaleDetail(BaseModel):
    sale = ForeignKeyField(Sale, field='sale_id')
    product = ForeignKeyField(Product, field='product_id')
    quantity = DecimalField(max_digits=10, decimal_places=2, null=False)
    subtotal = DecimalField(max_digits=10, decimal_places=2, null=False)
    
    class Meta:
        primary_key = CompositeKey('sale', 'product')
