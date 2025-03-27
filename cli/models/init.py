from .catalog.products import Product
from .people.clients import Client
from .transactions.sales import Sale
# ... otros modelos importantes

__all__ = ['Product', 'Client', 'Sale']  # Controla qué se exporta