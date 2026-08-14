"""Agenda de contactos en memoria."""
import re

_EMAIL_RE = re.compile(r"[^@\s]+@[^@\s]+\.[^@\s]+")


def validate_email(email):
    return bool(_EMAIL_RE.match(email)) if isinstance(email, str) else False


class ContactBook:
    def __init__(self):
        self._por_email = {}

    def add_contact(self, nombre, email):
        if not validate_email(email):
            raise ValueError("email invalido")
        if email in self._por_email:
            raise ValueError("email duplicado")
        self._por_email[email] = nombre
        return nombre

    def find_by_email(self, email):
        return self._por_email.get(email)

    def list_sorted(self):
        return sorted(self._por_email.values())
