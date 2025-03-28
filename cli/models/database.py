#CONFIGURACIÓN DE LA BASE DE DATOS
from peewee import MySQLDatabase
from dotenv import load_dotenv
import os
from peewee import Model

# Carga las variables del archivo .env
load_dotenv()

db = MySQLDatabase(
    os.getenv('DB_NAME'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    host=os.getenv('DB_HOST'),
    port=int(os.getenv('DB_PORT', 3306)),  # Valor por defecto si no existe
    charset='utf8mb4',
)

class BaseModel(Model):
    class Meta:
        database = db