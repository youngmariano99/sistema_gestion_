from models.database import BaseModel
from pewee import *
from models.catalog.categories import Category
from models.catalog.brands import Brand


class Product(BaseModel):
    product_id = AutoField(primary_key=True)
    name = CharField(max_length=100, null=False)
    stock = IntegerField(default=0)
    price = DecimalField(max_digits=10, decimal_places=2, null=False)
    cost = DecimalField(max_digits=10, decimal_places=2, null=False)
    category = ForeignKeyField(Category, field='category_id', null=True)


   # Relación muchos-a-muchos con Brand (tabla puente brands_products)
    brands = ManyToManyField(Brand, backref='products')   