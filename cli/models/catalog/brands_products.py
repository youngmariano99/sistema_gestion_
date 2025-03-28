from models.database import BaseModel
from models.catalog.products import Product
from models.catalog.brands import Brand
from peewee import *

class BrandProduct(BaseModel):
    product = ForeignKeyField(Product, field='product_id')
    brand = ForeignKeyField(Brand, field='brand_id')
    
    class Meta:
        primary_key = CompositeKey('product', 'brand')
