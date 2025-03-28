# Importa modelos principales para acceso directo:
# from models import Product, Client, etc.
from .catalog.products import Product
from .people.clients import Client
from .people.suppliers import Supplier
from .transaction.sales import Sale

__all__ = ['Product', 'Client', 'Supplier', 'Sale']  # Controla qué se exporta