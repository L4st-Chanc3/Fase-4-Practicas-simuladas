# main.py

import logging

from cliente import Cliente
from servicios import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)
from reserva import Reserva

from excepciones import (
    ClienteError,
    ServicioError,
    ReservaError
)


# Configuración del log
logging.basicConfig(
    filename="logs.txt",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def registrar_error(error):
    logging.error(error)
    print(f"ERROR: {error}")


print("\n===== SISTEMA SOFTWARE FJ =====\n")


# OPERACIÓN 1
try:
    cliente1 = Cliente("Kevin", "kevin@gmail.com", "3001234567")
    print(cliente1.mostrar_info())

except ClienteError as e:
    registrar_error(e)


# OPERACIÓN 2
try:
    cliente2 = Cliente("Al", "correo_malo", "abc")
    print(cliente2.mostrar_info())

except ClienteError as e:
    registrar_error(e)


# OPERACIÓN 3
try:
    servicio1 = ReservaSala("Sala VIP", 50000, 4)
    print(servicio1.descripcion())

except ServicioError as e:
    registrar_error(e)


# OPERACIÓN 4
try:
    servicio2 = AlquilerEquipo("Portátil Gamer", -10000, 2)

except ServicioError as e:
    registrar_error(e)


# OPERACIÓN 5
try:
    servicio3 = AsesoriaEspecializada(
        "Asesoría Python",
        80000,
        3
    )

    print(servicio3.descripcion())
    print("Costo con descuento:",
          servicio3.calcular_costo(0.10))

except ServicioError as e:
    registrar_error(e)


# OPERACIÓN 6
try:

    reserva1 = Reserva(cliente1, servicio1, 4)

    reserva1.confirmar()

    reserva1.procesar_reserva()

    print(reserva1.mostrar_reserva())

except ReservaError as e:
    registrar_error(e)


# OPERACIÓN 7
try:

    reserva2 = Reserva(cliente1, servicio3, -1)

except ReservaError as e:
    registrar_error(e)


# OPERACIÓN 8
try:

    reserva3 = Reserva(cliente1, servicio3, 3)

    reserva3.cancelar()

    reserva3.confirmar()

except ReservaError as e:
    registrar_error(e)


# OPERACIÓN 9
try:

    numero = 10 / 0

except ZeroDivisionError as e:
    registrar_error(e)


# OPERACIÓN 10
try:

    lista = [1, 2, 3]

    print(lista[10])

except IndexError as e:
    registrar_error(e)

finally:
    print("\nSistema finalizado correctamente")