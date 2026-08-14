"""Agenda de contactos en memoria."""
from contact_book.validation import validate_email


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
