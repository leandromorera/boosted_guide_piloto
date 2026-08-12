"""Comprueba que el andamiaje esta en pie.

Se puede borrar en cuanto exista la primera prueba de verdad. Existe para que la CI
del primer commit salga verde: una CI roja desde el minuto uno no distingue entre un
andamiaje mal montado y una tarea mal hecha.
"""


def test_el_andamiaje_esta_en_pie():
    assert True
