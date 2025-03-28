# --- Constantes de diseño ---
import os
import sys
from time import sleep
from typing import Optional
from colorama import Fore, Style, init
from enum import Enum


class Color:
    PRIMARY = Fore.CYAN
    SECONDARY = Fore.LIGHTMAGENTA_EX
    SUCCESS = Fore.LIGHTGREEN_EX
    WARNING = Fore.LIGHTYELLOW_EX
    DANGER = Fore.LIGHTRED_EX
    INFO = Fore.LIGHTBLUE_EX
    BORDER = Fore.LIGHTWHITE_EX

class MenuType(Enum):
    MAIN = "main"
    INVENTORY = "inventory"
    PEOPLE = "people"
    TRANSACTIONS = "transactions"

# --- Helpers visuales ---
def clear_console():
    """Limpia la consola manteniendo compatibilidad multiplataforma"""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_loading(message: str, duration: float = 1.5, steps: int = 3):
    """Muestra una animación de carga"""
    for i in range(steps):
        print(f"\r{Color.INFO}{message}{'.' * (i + 1)}", end="")
        sleep(duration / steps)
    print(Style.RESET_ALL)

def draw_menu_box(title: str, menu_type: MenuType):
    """Dibuja un cuadro decorado para el menú"""
    colors = {
        MenuType.MAIN: Color.PRIMARY,
        MenuType.INVENTORY: Color.SUCCESS,
        MenuType.PEOPLE: Color.SECONDARY,
        MenuType.TRANSACTIONS: Color.WARNING
    }
    color = colors.get(menu_type, Color.BORDER)
    
    title = f" {title} "
    border = "═" * (len(title) + 2)
    
    print(f"\n{color}╔{border}╗")
    print(f"║{Color.BORDER}{title.center(len(border))}{color}║")
    print(f"╚{border}╝{Style.RESET_ALL}\n")

def get_valid_input(prompt: str, min_val: int, max_val: int) -> Optional[int]:
    """Valida que la entrada sea un número dentro del rango"""
    while True:
        try:
            user_input = input(f"{Color.INFO}{prompt} {Style.RESET_ALL}")
            if user_input.lower() == 'q':
                return None
            value = int(user_input)
            if min_val <= value <= max_val:
                return value
            print(f"{Color.DANGER}Error: Ingrese un valor entre {min_val}-{max_val}")
        except ValueError:
            print(f"{Color.DANGER}¡Debe ser un número válido!")
        sleep(0.5)