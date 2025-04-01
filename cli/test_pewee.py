# Importa tus modelos y configura la base de datos
from models.catalog import Products, Brands, BrandsProducts # Asegúrate de importar tu modelo y conexión
from models.database import db
import logging

# Configura logging para ver las consultas SQL generadas
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('peewee')
logger.addHandler(logging.StreamHandler())

def test_queries():
    # Ejemplo 1: Consulta básica
    query = Products.select().where(Products.price > 10)
    print("SQL generado:", query)  # Muestra la consulta SQL sin ejecutarla
    
    # Ejemplo 2: Ejecutar la consulta y mostrar resultados
    print("\nProductos con precio > 10:")
    for product in query:  # ¡Aquí se ejecuta la consulta!
        print(f"- {product.name}: ${product.price}")

    # Ejemplo 3: Usar .execute() explícitamente (equivalente al bucle)
    print("\nMismo resultado con .execute():")
    for product in query.execute():
        print(f"- {product.name}: ${product.price}")

if __name__ == "__main__":
    test_queries()