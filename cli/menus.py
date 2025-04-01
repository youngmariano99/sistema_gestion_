import os
import sys
from time import sleep
from typing import Optional
from colorama import Fore, Style, init
from enum import Enum
from utils.views import Color, clear_console, show_loading , get_valid_input, draw_menu_box, MenuType
from controllers.intentory_ops import show_products, register_product, stock_refresh
# Inicializar colorama (para colores multiplataforma)
init(autoreset=True)



# --- Menús principales ---
def main_menu():
    while True:
        clear_console()
        draw_menu_box("SISTEMA DE GESTIÓN PRINCIPAL", MenuType.MAIN)
        
        print(f"{Color.PRIMARY}1. 📦 Gestión de Inventario")
        print(f"{Color.SECONDARY}2. 👥 Gestión de Personas")
        print(f"{Color.WARNING}3. 💰 Gestión de Transacciones")
        print(f"{Color.INFO}4. 📊 Reportes y Análisis")
        print(f"{Color.DANGER}5. 🚪 Salir del Sistema\n")
        
        choice = get_valid_input("► Seleccione una opción (1-5):", 1, 5)
        
        if choice == 1:
            inventory_menu()
        elif choice == 2:
            people_menu()
        elif choice == 3:
            transactions_menu()
        elif choice == 4:
            reports_menu()
        elif choice == 5:
            show_loading("Saliendo del sistema")
            clear_console()
            sys.exit(0)

# --- Submenús ---
def inventory_menu():
    while True:
        clear_console()
        draw_menu_box("GESTIÓN DE INVENTARIO", MenuType.INVENTORY)
        
        print(f"{Color.SUCCESS}1. 🆕 Registrar nuevo producto") #COMPLETADA (A MEJORAR)
        print(f"{Color.SUCCESS}2. 🔍 Buscar producto")
        print(f"{Color.SUCCESS}3. 📝 Listar todos los productos") #COMPLETADA (A MEJORAR)
        print(f"{Color.SUCCESS}4. 📦 Ajustar niveles de stock")
        print(f"{Color.SUCCESS}5. 🏷️ Actualizar precios")
        print(f"{Color.PRIMARY}0. ↩ Volver al menú principal\n")
        
        choice = get_valid_input("► Seleccione una opción (0-5):", 0, 5)
        
        if choice == 0:
            break
        elif choice == 1:
            show_loading("Cargando módulo de registro")
            register_product()
        elif choice == 2:
            show_loading("Buscando productos")
            # search_products()
        elif choice == 3:
            opción_elegida = ""
            show_loading("Mostrando productos")
            show_products()
            opción_elegida = input("Aprieta enter para continuar...")
            show_loading("Volviendo a menú de inventario")
        elif choice ==4:
            opción_elegida = ""
            show_loading("Cargando módulo de ajuste de stock")
            stock_refresh()
            opción_elegida = input("Aprieta enter para continuar...")
            show_loading("Volviendo a menú de inventario")



def people_menu():
    while True:
        clear_console()
        draw_menu_box("GESTIÓN DE PERSONAS", MenuType.PEOPLE)
        
        print(f"{Color.SECONDARY}1. 👤 Gestión de Clientes")
        print(f"{Color.SECONDARY}2. 🏭 Gestión de Proveedores")
        print(f"{Color.PRIMARY}0. ↩ Volver al menú principal\n")
        
        choice = get_valid_input("► Seleccione una opción (0-2):", 0, 2)
        
        if choice == 0:
            break
        elif choice == 1:
            clients_submenu()
        elif choice == 2:
            suppliers_submenu()

def clients_submenu():
    while True:
        clear_console()
        draw_menu_box("GESTIÓN DE CLIENTES", MenuType.PEOPLE)
        
        print(f"{Color.SECONDARY}1. 🆕 Registrar nuevo cliente")
        print(f"{Color.SECONDARY}2. 🔍 Buscar cliente por DNI")
        print(f"{Color.SECONDARY}3. 📋 Listar clientes frecuentes")
        print(f"{Color.SECONDARY}4. ✏️ Editar información")
        print(f"{Color.PRIMARY}0. ↩ Volver\n")
        
        choice = get_valid_input("► Seleccione una opción (0-4):", 0, 4)
        
        if choice == 0:
            break
        elif choice == 1:
            show_loading("Procesando registro de cliente")
            # register_client()

def suppliers_submenu():
    while True:
        clear_console()
        draw_menu_box("GESTIÓN DE PROVEEDORES", MenuType.PEOPLE)
        
        print(f"{Color.SECONDARY}1. 🆕 Registrar nuevo proveedor")
        print(f"{Color.SECONDARY}2. 🔍 Buscar proveedor por RUC")
        print(f"{Color.SECONDARY}3. 📋 Listar todos los proveedores")
        print(f"{Color.SECONDARY}4. ✏️ Editar información")
        print(f"{Color.PRIMARY}0. ↩ Volver\n")
        
        choice = get_valid_input("► Seleccione una opción (0-4):", 0, 4)
        
        if choice == 0:
            break
        elif choice == 1:
            show_loading("Procesando registro de proveedor")
            # register_supplier()

def transactions_menu():
    while True:
        clear_console()
        draw_menu_box("GESTIÓN DE TRANSACCIONES", MenuType.TRANSACTIONS)
        
        print(f"{Color.WARNING}1. 🛒 Registrar nueva venta")
        print(f"{Color.WARNING}2. 🛍️ Registrar nueva compra")
        print(f"{Color.WARNING}3. 🔄 Movimientos de inventario")
        print(f"{Color.WARNING}4. 📜 Historial de transacciones")
        print(f"{Color.PRIMARY}0. ↩ Volver al menú principal\n")
        
        choice = get_valid_input("► Seleccione una opción (0-4):", 0, 4)
        
        if choice == 0:
            break
        elif choice == 1:
            show_loading("Cargando módulo de ventas")
            # register_sale()
        elif choice == 2:
            show_loading("Cargando módulo de compras")
            # register_purchase()

def reports_menu():
    while True:
        clear_console()
        draw_menu_box("REPORTES Y ANÁLISIS", MenuType.REPORTS)
        
        print(f"{Color.INFO}1. 📈 Ventas por período")
        print(f"{Color.INFO}2. 📊 Compras por proveedor")
        print(f"{Color.INFO}3. 📦 Stock crítico")
        print(f"{Color.INFO}4. 💰 Margen de ganancia")
        print(f"{Color.INFO}5. 🏆 Productos más vendidos")
        print(f"{Color.PRIMARY}0. ↩ Volver al menú principal\n")
        
        choice = get_valid_input("► Seleccione una opción (0-5):", 0, 5)
        
        if choice == 0:
            break
        elif choice == 1:
            show_loading("Generando reporte de ventas")
            # sales_report()
        elif choice == 2:
            show_loading("Generando reporte de compras")
            # purchases_report()

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"\n{Color.DANGER}Operación cancelada por el usuario")
        sleep(1)
        clear_console()