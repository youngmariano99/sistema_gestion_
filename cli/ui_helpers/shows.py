from models.catalog import Category, Brands

#MOSTRAR CATEGORIAS
def show_categories():
    """Muestra todas las categorías disponibles con un número selector"""
    print("\nCategorías disponibles:")
    categorias = Category.select()
    for i, cat in enumerate(categorias, start=1):
        print(f"{i}. {cat.name}")
    return categorias

#MOSTRAR MARCAS
def show_brands():
    """Muestra todas las marcas disponibles"""
    print("\nMarcas disponibles:")
    brands = Brands.select()
    for i, brand in enumerate(brands, start=1):
        print(f"{i}. {brand.name}")
    return brands