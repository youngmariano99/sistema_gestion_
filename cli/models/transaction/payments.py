from models.database import BaseModel
from peewee import *

class PaymentMethod(BaseModel):
    payment_method_id = AutoField(primary_key=True)
    name = CharField(max_length=50, null=False)
    description = CharField(max_length=255, null=True)
