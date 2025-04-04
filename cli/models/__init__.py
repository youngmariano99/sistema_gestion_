# Importa modelos principales para acceso directo:
# from models import Product, Client, etc.
from .catalog import Products, Brands, BrandsProducts
from .people import Clients, Suppliers
from .inventory import StockMovementDetails, StockMovements
from .transaction import Sale, PurchaseDetail, Purchase, PaymentMethod

__all__ = ['Products', 'Brands', 'BrandsProducts', 'Clients', 'Suppliers', 'Sale', 'PurchaseDetail', 'Purchase', 'PaymentMethod', 'StockMovementDetails', 'StockMovements']  # Controla qué se exporta