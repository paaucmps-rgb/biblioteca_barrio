# catalogo.py

libros = [
    {"id": 1, "titulo": "Cien años de soledad", "estado": "Disponible", "accion": "Prestar"},
    {"id": 2, "titulo": "Don Quijote de la Mancha", "estado": "Prestado", "accion": "Devolver"}
]

def listar_libros():
    return libros

def agregar_libro(titulo):
    nuevo_id = len(libros) + 1
    nuevo_libro = {
        "id": nuevo_id,
        "titulo": titulo,
        "estado": "Disponible",
        "accion": "Prestar"
    }
    libros.append(nuevo_libro)