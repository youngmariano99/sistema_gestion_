from models.database import BaseModel
from pewee import Autofield, Charfield

class Brand(BaseModel):
    brand_id = AutoField(primary_key=True)
    name = CharField(max_length=50, unique=True, null=False)
    description = CharField(max_length=250, null=True)
