📦 Sistema de Gestión de Almacén (CLI)
Este es un sistema de gestión de almacén desarrollado en Python como una aplicación de línea de comandos (CLI). Se conecta a una base de datos MySQL mediante el ORM Peewee, facilitando la administración de inventarios.

📌 Sobre el Proyecto
Este sistema CLI fue desarrollado como un proyecto personal con el propósito de aprender y practicar Python, bases de datos MySQL y el uso de Peewee como ORM. Es un trabajo en progreso, con algunas funcionalidades completas y otras en desarrollo.
¡Si quieres probarlo, modificarlo o sugerir mejoras, eres bienvenido! 

🚀 Funcionalidades
El sistema cuenta con un menú interactivo que permite acceder a diferentes módulos. Actualmente, algunas funciones están completas y operativas, mientras que otras están en desarrollo.

📌 Gestión de Inventarios ✅
- Registrar nuevo producto → Permite registrar un nuevo producto y guardarlo en la base de datos.
- Buscar producto por nombre → Permite encontrar un producto específico mediante su nombre.
- Listar todos los productos → Muestra una lista de todos los productos registrados en el sistema.
- Editar productos → Posibilita la modificación de la información de un producto existente.
  
📌 Gestión de Personas 🚧 (En desarrollo)
- No hay funciones implementadas por el momento.
  
📌 Gestión de Transacciones 🚧 (En desarrollo)
- No hay funciones implementadas por el momento.
  
📌 Reportes y Análisis 🚧 (En desarrollo)
- No hay funciones implementadas por el momento.
  
⚙️ Requisitos
Para ejecutar el sistema, necesitas:
- Python 3.x
- MySQL
- Peewee
  
🛠 Instalación

1️⃣ Clona el repositorio:
git clone <URL_DEL_REPOSITORIO>


2️⃣ Instala las dependencias:
pip install -r requirements.txt


3️⃣ Configura la base de datos MySQL:

Notas importantes
Configuración inicial:
La base de datos usa codificación UTF8mb4 para soporte completo de caracteres
Todas las tablas tienen restricciones de integridad referencial

Validaciones:
Stock no puede ser negativo (CHECK (Stock >= 0))
Movimientos de stock deben tener cantidad positiva (CHECK (Quantity > 0))
Campos únicos: códigos de barras, nombres de categorías, nombres de marcas

Datos de ejemplo incluidos:
6 unidades de medida
30 categorías de productos
8 métodos de pago
2 marcas y 2 productos de ejemplo

Para implementar esta base de datos, simplemente ejecuta el script SQL completo en tu servidor MySQL. El sistema está diseñado para trabajar con MySQL 9.1.0 o superior.


4️⃣ Ejecuta el sistema:
python main.py


🎮 Uso

Al iniciar el sistema, aparecerá un menú principal donde puedes seleccionar una opción para gestionar el inventario.

📢 Contribuciones

Si deseas mejorar el proyecto, ¡envía un pull request! Todas las mejoras son bienvenidas. 💡

📜 Licencia
Este proyecto está bajo la Licencia MIT.


