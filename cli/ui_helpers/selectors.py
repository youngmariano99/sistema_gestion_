from .shows import show_categories, show_brands, show_unit_type
from models.catalog import Category, Brands, UnitTypes

#SELECCIÓN DE CATEGORÍA
def select_category():
    """Permite al usuario seleccionar una categoría por número"""
    
    categorias = show_categories()
    seleccion = input("\nLa categoria que necesitas se encuentra en la lista: siy/no: ").lower()
    if not categorias or seleccion == "no" :
        print("\nNo hay categorías existentes. ¿Deseas crear una ahora?")
        respuesta = input("(s/n): ").lower()
    
        if respuesta == 's':
            name = input("Ingresa el nombre de la nueva categoría: ").strip()

            # Creación CORRECTA usando el modelo Peewee
            try:
                new_category = Category.create(
                    name=name  # Asegúrate que 'name' sea el campo correcto en tu modelo
                )
                print(f"✅ Categoría '{name}' creada exitosamente!")
            
            except Exception as e:
                print(f"❌ Error al crear categoría: {e}")
                return None
        else:
            print("Operación cancelada.")
            return None
    
    while True:
        categorias = show_categories()
        try:
            seleccion = int(input("\nSelecciona el número de categoría: ")) - 1
            if 0 <= seleccion < len(categorias):
                return categorias[seleccion]
            print("¡Número fuera de rango! Intenta nuevamente.")
        except ValueError:
            print("¡Entrada inválida! Ingresa un número.")

#SELECCIÓN DE MARCAS
def select_brands():
    """Permite seleccionar una o más marcas"""
    brands = show_brands()
    selected = []
    seleccion = input("\nLa marca que necesitas se encuentra en la lista?: si/no: ").lower()
   

    if not brands or seleccion == "no":
        print("\nNo hay marcas existentes. ¿Deseas crear una ahora?")
        respuesta = input("(s/n): ").lower()
    
        if respuesta == "s":
            name = input("Ingresa el nombre de la nueva marca: ").strip()
            description = input("Ingrese una descripción de la marca(opcional), No más de 250 caracteres: ")
        
        # Creación CORRECTA usando el modelo Peewee
            try:
                new_brand = Brands.create(
                    name=name,
                    description=description
                )
                print(f"✅ Marca '{name}' creada exitosamente!")
                
            except Exception as e:
                print(f"❌ Error al crear categoría: {e}")
                return None
        else:
            print("Operación cancelada.")
            return None
    
    while True:
        brands = show_brands()
        try:
            seleccion = input("\nSelecciona número(s) de marca (separados por coma ej: 1,2,3): ")
            indices = [int(s.strip())-1 for s in seleccion.split(',')]
            
            if all(0 <= i < len(brands) for i in indices):
                selected = [brands[i] for i in indices]
                return selected
            else:    
                print("¡Algún número fuera de rango! Intenta nuevamente.")
        except ValueError:
            print("¡Entrada inválida! Ingresa números separados por comas.")


def select_unit_type():
    """Permite seleccionar una o más marcas"""
    unit_type = show_unit_type()
    seleccion = input("\nLa unidad que necesitas se encuentra en la lista?: si/no: ").lower()
   

    if not unit_type or seleccion == "no":
        print("\nNo existe la unidad necesaria. ¿Deseas crear una ahora?")
        respuesta = input("(s/n): ").lower()
    
        if respuesta == "s":
            name = input("Ingresa el nombre de la nueva unidad: ").strip()
            symbol = input("Ingrese el simbolo que representa la unidad (Ej:Kilogramos = Kg): ").strip().lower()
        
        # Creación CORRECTA usando el modelo Peewee
            try:
                new_unit_type = UnitTypes.create(
                    name=name,
                    symbol=symbol
                )
                print(f"✅ Unidad '{name}' creada exitosamente!")
                
            except Exception as e:
                print(f"❌ Error al crear categoría: {e}")
                return None
        else:
            print("Operación cancelada.")
            return None
    
    while True:
        unit_type = show_unit_type()
        try:
            seleccion = int(input("\nSelecciona el número de la unidad: ")) - 1
            if 0 <= seleccion < len(unit_type):
                return unit_type[seleccion]
            print("¡Número fuera de rango! Intenta nuevamente.")
        except ValueError:
            print("¡Entrada inválida! Ingresa un número.")
    
      