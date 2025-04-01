from models.database import BaseModel
from peewee import *

class Suppliers(BaseModel):
    supplier_id = AutoField(primary_key=True)
    name = CharField(max_length=100, null=False)
    description = CharField(max_length=255, null=True)
    phone = CharField(max_length=20, null=True)