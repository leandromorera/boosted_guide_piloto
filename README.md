# boosted_guide_piloto

Proyecto generado por Boosted Guide

Generado por Boosted Guide a partir de una especificacion. La estructura y las firmas salen del
esquema del proyecto; los cuerpos los escriben las tareas.

## Como se trabaja aqui

- `main` esta protegida: nada entra sin pull request, revision y CI en verde.
- Cada tarea vive en su rama `task/<id>` y se integra en `run/<run_id>`, de una en una.
- Los ficheros de contrato —los que importan varios— **no se tocan desde una tarea**. Si hay que
  cambiar una firma, es una tarea de contrato aparte, porque afecta a todo el mundo.

## Comprobar

```
pip install -r requirements.txt
pytest -q
```

Es el mismo comando que ejecuta la CI y el mismo que ejecuta el pipeline al validar una tarea.
