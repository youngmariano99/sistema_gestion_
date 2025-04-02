#FUNCIONES CRUD Y LÓGICA DE NEGOCIO
from models.database import db
from models.catalog import BrandsProducts, Products, Category
from ui_helpers.selectors import select_category, select_brands
from utils.views import clear_console, draw_menu_box, MenuType, Color, show_loading
from peewee import DoesNotExist



#FUNCIÓN PARA PROBAR LA CONEXIÓN DE LA BASE DE DATOS
def init_db():
    try:
        db.connect()
        print(" DB conectada")
    except Exception as e:
        print(f" Error de conexión: {e}")
        exit(1)

#FUNCIÓN PARA BUSCAR PRODUCTOS
def search_products(): 
    nombre_producto = input("Coloque el nombre del producto que quiera ver: ")
    
    # Realizar la consulta (búsqueda insensible a mayúsculas/minúsculas)
    query = Products.select().where(Products.name ** f"%{nombre_producto}%")
    
    # Obtener todos los resultados
    resultados = list(query)
    
    if not resultados:
        print(f"\n❌ No se encontraron productos con el nombre: '{nombre_producto}'")
        return
    
    print(f"\n🔍 Resultados para '{nombre_producto}':")
    for producto in resultados:
        print(f"\nID: {producto.product_id}")
        print(f"Nombre: {producto.name}")
        print(f"Stock: {producto.stock}")
        print(f"Precio: ${producto.price:.2f}")
        print(f"Categoría: {producto.category.name if producto.category else 'Sin categoría'}")
    
    
    

#FUNCIÓN PARA MOSTRAR TODOS LOS PRODUCTOS
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

#FUNCIÓN PARA EDITAR LOS PRODUCTOS
def edit_product():
    while True:
        try:
            # Mostrar lista de productos
            print("Productos:")
            products = Products.select()
            for product in products:
                print(product.product_id, product.name)
            
            # Obtener ID del producto
            producto_id = int(input("\nIngrese el ID del producto a modificar (0 para salir): "))
            if producto_id == 0:
                break
                
            clear_console()
            
            # Verificar existencia del producto
            producto = Products.get_by_id(producto_id)
            print(f"\nProducto elegido: {producto.name} (Stock actual: {producto.stock})")

            while True:
                try:
                    clear_console()
                    draw_menu_box("EDITAR PRODUCTO", MenuType.INVENTORY)
                
                    print(f"{Color.SUCCESS}1. ✏️ Cambiar nombre")
                    print(f"{Color.SUCCESS}2. 🏷️ Cambiar precio")
                    print(f"{Color.SUCCESS}3. 📦 Cambiar stock")
                    print(f"{Color.SUCCESS}4. 💰 Cambiar costo")
                    print(f"{Color.SUCCESS}5. 🏷️ Cambiar categoría")
                    print(f"{Color.PRIMARY}0. ↩ Volver a lista de productos")
                    
                    eleccion = int(input("\nEscriba su elección: "))
                    
                    if eleccion == 0:
                        break
                        
                    elif eleccion == 1:
                        nuevo_nombre = input("Ingrese el nuevo nombre: ")
                        Products.update(name=nuevo_nombre).where(Products.product_id == producto_id).execute()
                        print(f"✅ Nombre actualizado a: {nuevo_nombre}")
                        
                    elif eleccion == 2:
                        nuevo_precio = float(input("Ingrese el nuevo precio (Ej: 999.99): ").replace(',', '.'))
                        Products.update(price=nuevo_precio).where(Products.product_id == producto_id).execute()
                        print(f"✅ Precio actualizado a: {nuevo_precio}")
                        
                    elif eleccion == 3:
                        nuevo_stock = int(input("Ingrese el nuevo stock: "))
                        Products.update(stock=nuevo_stock).where(Products.product_id == producto_id).execute()
                        print(f"✅ Stock actualizado a: {nuevo_stock}")
                        
                    elif eleccion == 4:
                        nuevo_costo = float(input("Ingrese el nuevo costo (Ej: 999.99): ").replace(',', '.'))
                        Products.update(cost=nuevo_costo).where(Products.product_id == producto_id).execute()
                        print(f"✅ Costo actualizado a: {nuevo_costo}")
                        
                    elif eleccion == 5:
                        category_nueva = select_category()
                        if category_nueva:
                            Products.update(category=category_nueva).where(Products.product_id == producto_id).execute()
                            print(f"✅ Categoría actualizada a: {category_nueva.name}")
                            
                    input("\nPresione Enter para continuar...")
                    
                except ValueError:
                    print("❌ Error: Debes ingresar un número válido.")
                    input("Presione Enter para continuar...")
                except Exception as e:
                    print(f"❌ Error inesperado: {e}")
                    input("Presione Enter para continuar...")
                    
        except ValueError:
            print("❌ Error: Debes ingresar un número válido para el ID.")
        except DoesNotExist:
            print(f"❌ Error: No existe un producto con ID {producto_id}.")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
        finally:
            input("Presione Enter para continuar...")
            clear_console()


    
    


