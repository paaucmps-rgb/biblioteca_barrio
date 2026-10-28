# main.py
from catalogo import Catalogo
from socios import Socios
from prestamos import Prestamos

def iniciar_sistema():
    catalogo = Catalogo()
    socios = Socios()
    prestamos = Prestamos(catalogo, socios)

    # Datos iniciales de prueba
    catalogo.agregar_ejemplar("E01", "Cien Años de Soledad", "Gabriel García Márquez")
    catalogo.agregar_ejemplar("E02", "Cien Años de Soledad", "Gabriel García Márquez") # Copia 2
    catalogo.agregar_ejemplar("E03", "El Quijote", "Miguel de Cervantes")
    
    socios.registrar_socio("S01", "Ana Pérez")

    while True:
        print("\n--- BIBLIOTECA DE BARRIO ---")
        print("1. Buscar libro")
        print("2. Dar de alta socio")
        print("3. Realizar préstamo")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Ingrese el título a buscar: ")
            resultados = catalogo.buscar(titulo)
            print(f"\nResultados para '{titulo}':")
            for e in resultados:
                print(f"ID: {e.id} | Título: {e.titulo} | Estado: {e.estado}")

        elif opcion == "2":
            id_s = input("ID del socio: ")
            nombre = input("Nombre del socio: ")
            if socios.registrar_socio(id_s, nombre):
                print("Socio registrado con éxito.")
            else:
                print("El ID de socio ya existe.")

        elif opcion == "3":
            id_s = input("ID del socio: ")
            id_e = input("ID del ejemplar del libro: ")
            exito, mensaje = prestamos.realizar_prestamo(id_e, id_s)
            print(mensaje)

        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    iniciar_sistema()