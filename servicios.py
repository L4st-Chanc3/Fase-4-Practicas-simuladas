# servicios.py

from abc import ABC, abstractmethod
from excepciones import ServicioError


# Clase abstracta
class Servicio(ABC):

    def __init__(self, nombre, precio_base):

        if precio_base <= 0:
            raise ServicioError("El precio base debe ser mayor que cero")

        self.nombre = nombre
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def descripcion(self):
        pass


# Servicio 1
class ReservaSala(Servicio):

    def __init__(self, nombre, precio_base, horas):
        super().__init__(nombre, precio_base)

        if horas <= 0:
            raise ServicioError("Las horas deben ser mayores a cero")

        self.horas = horas

    def calcular_costo(self):
        return self.precio_base * self.horas

    def descripcion(self):
        return f"Reserva de sala por {self.horas} horas"


# Servicio 2
class AlquilerEquipo(Servicio):

    def __init__(self, nombre, precio_base, dias):
        super().__init__(nombre, precio_base)

        if dias <= 0:
            raise ServicioError("Los días deben ser mayores a cero")

        self.dias = dias

    def calcular_costo(self):
        return self.precio_base * self.dias

    def descripcion(self):
        return f"Alquiler de equipo por {self.dias} días"


# Servicio 3
class AsesoriaEspecializada(Servicio):

    def __init__(self, nombre, precio_base, horas):
        super().__init__(nombre, precio_base)

        if horas <= 0:
            raise ServicioError("Las horas deben ser válidas")

        self.horas = horas

    # Método sobrecargado mediante parámetro opcional
    def calcular_costo(self, descuento=0):

        total = self.precio_base * self.horas

        if descuento > 0:
            total -= total * descuento

        return total

    def descripcion(self):
        return f"Asesoría especializada durante {self.horas} horas"