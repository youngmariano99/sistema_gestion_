from models.database import BaseModel
from peewee import *

class Clients(BaseModel):
    client_id = AutoField(primary_key=True)
    name = CharField(max_length=50, null=False)
    surname = CharField(max_length=50, null=False)
    phone = CharField(max_length=20, unique=True, null=True)
    email = CharField(max_length=100, unique=True, null=True)