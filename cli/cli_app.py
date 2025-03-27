#PROGRAMA PRINCIPAL CLI
from models.database import db


def init_db():
    db.connect()
    # db.create_tables([User])  # Solo si necesitas crear tablas

if __name__ == '__main__':
    init_db()
    