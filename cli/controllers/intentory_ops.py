#FUNCIONES CRUD Y LÓGICA DE NEGOCIO
from models.database import db
from models.catalog import Category

#Función para probar la conexión de la base de datos
def init_db():
    try:
        db.connect()
        print(" DB conectada")
    except Exception as e:
        print(f" Error de conexión: {e}")
        exit(1)

def show_products():
    categories = Category.select()  # Usa un nombre diferente para la variable
    for category in categories:
        print(category.name)
