# reserva.py

from excepciones import ReservaError


class Reserva:

    def __init__(self, cliente, servicio, duracion):

        if duracion <= 0:
            raise ReservaError("La duración debe ser mayor que cero")

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):

        if self.estado == "Cancelada":
            raise ReservaError("No se puede confirmar una reserva cancelada")

        self.estado = "Confirmada"

    def cancelar(self):
        self.estado = "Cancelada"

    def procesar_reserva(self):

        try:

            costo = self.servicio.calcular_costo()

            print("Procesando reserva...")
            print(self.cliente.mostrar_info())
            print(self.servicio.descripcion())
            print(f"Costo total: ${costo}")

        except Exception as e:
            raise ReservaError("Error al procesar la reserva") from e

    def mostrar_reserva(self):

        return (
            f"Cliente: {self.cliente.get_nombre()} | "
            f"Servicio: {self.servicio.nombre} | "
            f"Estado: {self.estado}"
        )