from models.database import BaseModel
from peewee import *

class Brands(BaseModel):
    brand_id = AutoField(primary_key=True)
    name = CharField(max_length=50, unique=True, null=False)
    description = CharField(max_length=250, null=True)
