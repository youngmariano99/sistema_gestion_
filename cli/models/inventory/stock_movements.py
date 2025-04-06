from models.database import BaseModel
from peewee import *
from models.catalog.products import Products
from datetime import datetime  # Para usar datetime.now()

class StockMovements(BaseModel):
    movement_id = AutoField(primary_key=True)
    product = ForeignKeyField(Products, field='product_id', null=True)
    quantity = DecimalField(max_digits=10, decimal_places=2, null=False)
    type = CharField(choices=['ENTRADA', 'SALIDA', 'AJUSTE'])
    date = DateTimeField(null=False, default=datetime.now)
    reason = CharField(max_length=255, null=True)

class StockMovementDetails(BaseModel):
    movement = ForeignKeyField(StockMovements, field='movement_id')
    product = ForeignKeyField(Products, field='product_id')
    quantity = DecimalField(max_digits=10, decimal_places=2, null=False)
    
    class Meta:
        primary_key = CompositeKey('movement', 'product')
        table_name = 'stock_movement_details'
