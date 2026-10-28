# prestamos.py
from datetime import datetime, timedelta

# ==========================================
# DIARIO / DECISIÓN DEL CLIENTE:
# "No permitiremos que Prestamos lea directamente la lista interna de Catalogo. 
# Mantendremos el uso exclusivo de funciones públicas para preservar el encapsulamiento."
# ==========================================

class PrestamoInfo:
    def __init__(self, id_ejemplar, id_socio):
        self.id_ejemplar = id_ejemplar
        self.id_socio = id_socio
        self.fecha_prestamo = datetime.now()
        # Cada préstamo caduca a los 7 días
        self.fecha_caducidad = self.fecha_prestamo + timedelta(days=7)

class Prestamos:
    def __init__(self, catalogo_comp, socios_comp):
        self.catalogo = catalogo_comp
        self.socios = socios_comp
        self.historial_prestamos = []

    def realizar_prestamo(self, id_ejemplar, id_socio):
        # 1. Comprobar si el socio puede pedir libros (usando función pública)
        if not self.socios.puede_pedir(id_socio):
            return False, "Socio no autorizado (sancionado, no existe o límite de 2 libros alcanzado)."

        # 2. Obtener el ejemplar (usando función pública de catalogo)
        ejemplar = self.catalogo.obtener(id_ejemplar)
        if not ejemplar:
            return False, "El ejemplar especificado no existe."
        
        if ejemplar.estado == "prestado":
            return False, "El ejemplar está prestado. ¿Desea reservarlo?"
        if ejemplar.estado == "reservado":
            return False, "El ejemplar está reservado."

        # 3. Marcar prestado y registrar
        self.catalogo.marcar_prestado(id_ejemplar)
        self.socios.agregar_prestamo_socio(id_socio, id_ejemplar)
        
        prestamo = PrestamoInfo(id_ejemplar, id_socio)
        self.historial_prestamos.append(prestamo)
        
        caducidad_str = prestamo.fecha_caducidad.strftime("%Y-%m-%d")
        return True, f"Préstamo exitoso. Caduca el {caducidad_str}."