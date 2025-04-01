#FUNCIONES CRUD Y LÓGICA DE NEGOCIO
from models.database import db
from models.catalog import BrandsProducts, Products, Category
from ui_helpers.selectors import select_category, select_brands
from utils.views import clear_console
from peewee import DoesNotExist

#Función para probar la conexión de la base de datos
def init_db():
    try:
        db.connect()
        print(" DB conectada")
    except Exception as e:
        print(f" Error de conexión: {e}")
        exit(1)

def show_products():
    products = Products.select()  # Usa un nombre diferente para la variable
    for product in products:
        print(product.name)



#FUNCIÓN PARA REGISTRAR PRODUCTO

def register_product():
    print("\n" + "="*50)
    print("REGISTRO DE NUEVO PRODUCTO".center(50))
    print("="*50 + "\n")
    
    # Datos básicos
    name = input("Ingresa el nombre del producto: ")
    
    try:
        stock = int(input("Ingresa el stock (0 default): ") or 0)
        price = float(input("Ingresa el precio (Ej: 999.99): ").replace(',', '.'))
        cost = float(input("Ingresa el costo (Ej: 999.99): ").replace(',', '.'))
    except ValueError:
        print("¡Error en los datos numéricos! Intenta nuevamente.")
        return
    
    category = select_category()
    if category == None:  # Si el usuario canceló o no hay categorías
        print("\n⚠️ Operación cancelada. No se ha seleccionado categoría.")
        return  # Salimos de la función
    selected_brands = select_brands()
    if selected_brands == None:  # Si el usuario canceló o no hay categorías
        print("\n⚠️ Operación cancelada. No se ha seleccionado categoría.")
        return  # Salimos de la función
    print(f"\nResumen: {name} | Stock: {stock} | Precio: ${price:.2f} | Costo: ${cost:.2f}")
    print(f"Categoría: {category.name}")
    print("Marcas:", ", ".join([b.name for b in selected_brands]))
    
    confirmar = input("\n¿Confirmar registro? (s/n): ").lower()

    if confirmar == 's':
        Temp_Product = Products.create(
            name=name,
            stock=stock,
            price=price,
            cost=cost,
            category=category
        )
    for brand in selected_brands:
        BrandsProducts.create(
            products= Temp_Product,
            brands=brand
        )
        print("¡Producto registrado exitosamente!")
    else:
        print("Registro cancelado.")

def stock_refresh():
    print("Productos:")
    products = Products.select()  # Usa un nombre diferente para la variable
    for product in products:
        print(product.product_id, product.name)

    
    
    try:
        # Paso 1: Pedir ID y validar que sea un número
        producto_id = int(input("Ingrese el ID del producto a modificar: "))
        clear_console()
     
        
        # Paso 2: Verificar si el producto existe antes de actualizar
        producto = Products.get_by_id(producto_id)  # Busca el producto (ejecución inmediata)
        print(f"\nProducto elegido: {producto.name} (Stock actual: {producto.stock})")
        nuevo_stock = int(input("Ingrese el nuevo stock: "))
        
        # Paso 3: Actualizar el precio
        Products.update(stock=nuevo_stock).where(Products.product_id == producto_id).execute()
        print(f"✅ Stock del producto {producto.stock} actualizado a {nuevo_stock}")

    except ValueError:
        print("❌ Error: Debes ingresar un número válido para el ID y el precio.")
    except DoesNotExist:
        print(f"❌ Error: No existe un producto con ID {producto_id}.")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")


