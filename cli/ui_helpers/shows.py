from models.catalog import Category, Brands, UnitTypes


#MOSTRAR CATEGORIAS
def show_categories():
    """Muestra todas las categorías disponibles con un número selector"""
    print("\nCategorías disponibles:")
    categorias = list(Category.select())
    for i, cat in enumerate(categorias, start=1):
        print(f"{i}. {cat.name}")
    return categorias

#MOSTRAR MARCAS
def show_brands():
    """Muestra todas las marcas disponibles"""
    print("\nMarcas disponibles:")
    brands = list(Brands.select())
    for i, brand in enumerate(brands, start=1):
        print(f"{i}. {brand.name}")
    return brands

def show_unit_type():
    """Muestra todas las unidades disponibles"""
    print("\nUnidades disponibles:")
    unit_type = list(UnitTypes.select())
    for i, units in enumerate(unit_type, start=1):
        print(f"{i}. {units.name} {units.symbol}")
        
    return unit_type