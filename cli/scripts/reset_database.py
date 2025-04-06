#!/usr/bin/env python3
# scripts/reset_database.py

from peewee import * # Ajusta los imports según tu estructura
from models.database import db
from models.catalog.products import  Products
from models.catalog.brands import Brands
from models.catalog.brands_products import BrandsProducts
from models.catalog.categories import Category
#ANTES DEL RESET HACER UN BACKUP:
# mysqldump -u root -p sistema_gestion_may > "backup_sistema_almacen_$(Get-Date -Format 'yyyyMMdd').sql" -> en la consonla

def reset_data():
    try:
        print("⚠️ ADVERTENCIA: Esto borrará TODOS los registros.")
        confirmar = input("¿Continuar? (s/n): ").lower()
        
        if confirmar != 's':
            print("Operación cancelada.")
            return

        # Desactivar FKs (MySQL)
        db.execute_sql('SET FOREIGN_KEY_CHECKS=0;')
        
        # Borrar datos en orden seguro
        # BrandsProducts.delete().execute()  # Primero relaciones
        # Products.delete().execute()
        # Brands.delete().execute()
        Category.delete().execute()
        # Añade otras tablas si es necesario

        # Reactivar FKs
        db.execute_sql('SET FOREIGN_KEY_CHECKS=1;')
        
        print("✅ Todos los registros eliminados (estructura conservada).")
    
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        db.rollback()  # Revierte cambios si hay error

if __name__ == '__main__':
    reset_data()
    input("\nPresiona Enter para salir...")