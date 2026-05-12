# excepciones.py

class ClienteError(Exception):
    """Excepción personalizada para errores de clientes"""
    pass


class ServicioError(Exception):
    """Excepción personalizada para errores de servicios"""
    pass


class ReservaError(Exception):
    """Excepción personalizada para errores de reservas"""
    pass