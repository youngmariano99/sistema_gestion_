from models.database import BaseModel
from peewee import *
from models.catalog.products import Product
from datetime import datetime  # Para usar datetime.now()

class StockMovement(BaseModel):
    movement_id = AutoField(primary_key=True)
    product = ForeignKeyField(Product, field='product_id', null=True)
    quantity = DecimalField(max_digits=10, decimal_places=2, null=False)
    type = CharField(choices=['Ingreso', 'Salida', 'Ajuste'], null=False)
    date = DateTimeField(null=False, default=datetime.now)
    reason = CharField(max_length=255, null=True)

class StockMovementDetail(BaseModel):
    movement = ForeignKeyField(StockMovement, field='movement_id')
    product = ForeignKeyField(Product, field='product_id')
    quantity = DecimalField(max_digits=10, decimal_places=2, null=False)
    
    class Meta:
        primary_key = CompositeKey('movement', 'product')
