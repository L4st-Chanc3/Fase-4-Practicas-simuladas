# cliente.py

from excepciones import ClienteError


class Cliente:

    def __init__(self, nombre, correo, telefono):

        # Encapsulación
        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

        self.validar_datos()

    def validar_datos(self):

        if len(self.__nombre.strip()) < 3:
            raise ClienteError("El nombre debe tener mínimo 3 caracteres")

        if "@" not in self.__correo:
            raise ClienteError("Correo electrónico inválido")

        if not self.__telefono.isdigit():
            raise ClienteError("El teléfono solo debe contener números")

    # Getters
    def get_nombre(self):
        return self.__nombre

    def get_correo(self):
        return self.__correo

    def get_telefono(self):
        return self.__telefono

    def mostrar_info(self):
        return f"Cliente: {self.__nombre} | Correo: {self.__correo}"