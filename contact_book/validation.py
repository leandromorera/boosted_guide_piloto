"""Validacion de datos de contacto."""
import re

_EMAIL = re.compile(r"^[^@\s]+@[^@\s]+\.[a-zA-Z]{2,}$")


def validate_email(email: str) -> bool:
    """Si el email tiene una forma admisible.

    Se valida la forma, no la existencia: comprobar que un buzon existe requiere mandarle algo, y
    eso no es trabajo de una funcion de dominio.
    """
    if not isinstance(email, str):
        return False
    return bool(_EMAIL.match(email.strip()))
