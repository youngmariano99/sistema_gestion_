from models import database, catalog, inventory,people,transaction  # Importa lo que necesites
from controllers.intentory_ops import init_db
from menus import main_menu

def main():
    init_db()  # Verifica conexión
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\nOperación cancelada")  # Implementa esto en operations.py

if __name__ == '__main__':
    main()
