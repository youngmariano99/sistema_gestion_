from models.database import BaseModel
from models.catalog.products import Products
from models.catalog.brands import Brands
from peewee import *

class BrandsProducts(BaseModel):
    products = ForeignKeyField(
        Products,
        field='product_id',  # ⬅ Nombre real de la columna en Brands_Products
        column_name='product_id'  # ⬅ ¡Forzar el nombre de columna en la tabla!
    )
    brands = ForeignKeyField(
        Brands,
        field='brand_id',    # ⬅ Nombre real de la columna en Brands_Products
        column_name='brand_id'  # ⬅ ¡Forzar el nombre de columna en la tabla!
    )
    
    class Meta:
        primary_key = CompositeKey('products', 'brands')
        table_name = 'brands_products'
