from models.database import BaseModel
from pewee import *

class Category(BaseModel):
    category_id = AutoField(primary_key=True)
    name = CharField(max_length=50, unique=True, null=False)
