from models.database import BaseModel
from peewee import *
from models.people.suppliers import Supplier
from models.transaction.payments import PaymentMethod
from models.catalog.products import Product

class Purchase(BaseModel):
    purchase_id = AutoField(primary_key=True)
    supplier = ForeignKeyField(Supplier, field='supplier_id', null=True)
    date = DateTimeField(null=False, default=datetime.now)
    total = DecimalField(max_digits=10, decimal_places=2, null=False)
    payment_method = ForeignKeyField(PaymentMethod, field='payment_method_id', null=True)

class PurchaseDetail(BaseModel):
    purchase = ForeignKeyField(Purchase, field='purchase_id')
    product = ForeignKeyField(Product, field='product_id')
    quantity = DecimalField(max_digits=10, decimal_places=2, null=False)
    subtotal = DecimalField(max_digits=10, decimal_places=2, null=False)
    
    class Meta:
        primary_key = CompositeKey('purchase', 'product')
