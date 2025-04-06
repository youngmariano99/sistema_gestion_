from models.database import BaseModel
from peewee import *


class UnitTypes(BaseModel):
    unit_id = AutoField(primary_key=True)
    name = CharField(max_length=20, unique=True)
    symbol = CharField(max_length=5, null=True)
    class Meta:
        table_name = "unit_types"
        