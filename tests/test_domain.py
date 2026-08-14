"""Pruebas del dominio de la agenda de contactos.

Usa lo que declara contact_book/domain.py en lugar de reimplementar la logica.
"""

from __future__ import annotations

import pytest

from contact_book.domain import Contact, ContactBook


def test_add_contact_valid():
    book = ContactBook()
    book.add_contact("Alice", "alice@example.com")
    assert book.find_by_email("alice@example.com") is not None


def test_add_contact_invalid_email():
    book = ContactBook()
    with pytest.raises(ValueError):
        book.add_contact("Bob", "no-es-un-email")


def test_find_by_email_existing():
    book = ContactBook()
    book.add_contact("Alice", "alice@example.com")
    contact = book.find_by_email("alice@example.com")
    assert contact is not None
    assert contact.email == "alice@example.com"
    assert contact.name == "Alice"


def test_find_by_email_non_existing():
    book = ContactBook()
    assert book.find_by_email("nadie@example.com") is None


def test_list_sorted_alphabetical():
    book = ContactBook()
    book.add_contact("Charlie", "charlie@example.com")
    book.add_contact("Alice", "alice@example.com")
    book.add_contact("Bob", "bob@example.com")
    contacts = book.list_sorted_alphabetical()
    assert [c.name for c in contacts] == ["Alice", "Bob", "Charlie"]
