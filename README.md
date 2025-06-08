# InventarioDB

## Descripción
Este proyecto pone en marcha un pequeño servidor MCP (Model Context Protocol) que gestiona un inventario de productos usando SQLite.  
Cada función decorada con `@mcp.tool()` expone una "herramienta" que puede ser invocada por un cliente MCP para crear, leer, actualizar o eliminar productos.

## Características
- Gestión completa de inventario (CRUD)
- Base de datos SQLite para almacenamiento persistente
- API RESTful a través de MCP
- Fácil integración con clientes MCP
- Validación de datos
- Manejo de errores robusto

## Requisitos
- Python 3.7 o superior  
- SQLite (incluido en la biblioteca estándar de Python)  

## Instalación

1. Clona o descarga este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/inventariodb.git
   cd inventariodb
   ```

2. Instala Claude desktop:
   https://claude.ai/download

3. Instala las dependencias:
   ```bash
   pip install uv
   uv add "mcp[cli]"
   uv run mcp install main.py
   ```

## API de Herramientas MCP

### Crear Producto
```python
@mcp.tool()
def crear_producto(nombre: str, cantidad: int, precio: float) -> dict
```
Crea un nuevo producto en el inventario.

### Obtener Producto
```python
@mcp.tool()
def obtener_producto(id: int) -> dict
```
Obtiene la información de un producto específico.

### Actualizar Producto
```python
@mcp.tool()
def actualizar_producto(id: int, nombre: str = None, cantidad: int = None, precio: float = None) -> dict
```
Actualiza la información de un producto existente.

### Eliminar Producto
```python
@mcp.tool()
def eliminar_producto(id: int) -> bool
```
Elimina un producto del inventario.

## Estructura del Proyecto
```
inventariodb/
├── server.py          # Servidor MCP principal
├── database.py        # Configuración y operaciones de base de datos
├── requirements.txt   # Dependencias del proyecto
└── README.md         # Este archivo
```