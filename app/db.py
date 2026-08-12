"""app/db.py

Contrato generado a partir del esquema del proyecto. Define la forma —nombres, parametros y
tipos— que el resto del codigo importa.

No implementes aqui: este fichero lo comparten todas las tareas, y cambiarlo obliga a coordinar a
todo el mundo. Si necesitas cambiar una firma, es una tarea de contrato aparte.
"""

from __future__ import annotations


def sesion() -> Session:
    """Abre una sesion contra la base."""
    raise NotImplementedError("sesion")
