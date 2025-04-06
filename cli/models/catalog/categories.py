from models.database import BaseModel
from peewee import *

class Category(BaseModel):
    category_id = AutoField(primary_key=True)
    name = CharField(max_length=50, unique=True, null=False)
    is_perishable = BooleanField(default=False)  
    description = TextField(null=True)  

    class Meta:
        table_name = 'category'
