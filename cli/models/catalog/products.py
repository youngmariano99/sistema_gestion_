from models.database import BaseModel
from peewee import *
from models.catalog.categories import Category
from models.catalog.unit_types import UnitTypes




class Products(BaseModel):
    product_id = AutoField(primary_key=True, column_name='Product_ID')
    name = CharField(max_length=100, null=False, column_name='Name')
    stock = IntegerField(default=0, column_name='Stock')
    price = DecimalField(max_digits=10, decimal_places=2, null=False, column_name='Price')
    cost = DecimalField(max_digits=10, decimal_places=2, null=False, column_name='Cost')
    category = ForeignKeyField(Category, field='category_id', null=True, column_name='Category_ID')
    min_stock = IntegerField(default=0, column_name='Min_Stock')  
    barcode = CharField(max_length=50, null=True, column_name='Barcode')  
    is_active = BooleanField(default=True, column_name='Is_Active')  
    expiration_date = DateField(null=True, column_name='Expiration_Date')  
    unit = ForeignKeyField(UnitTypes, field='unit_id', column_name='Unit_Id')  
    class Meta:
        table_name = 'products'  # Asegúrate que coincida exactamente con tu tabla en MySQL
        legacy_table_names = False  # Desactiva comportamientos heredados
        
    #def get_brands(self):
      #  """Método simple para obtener las marcas de ESTE producto"""
     #   return (Brands.select()
      #              .join(BrandsProducts)
       #             .where(BrandsProducts.products == self)) 
                  

