# Vistas genéricas en Django: CRUD de productos

CRUD completo de productos con las vistas basadas en clases que trae Django.

## Tecnologías

- Python y Django 6.1
- SQLite

## Vistas

| Ruta | Vista | Qué hace |
|---|---|---|
| `/` | `ListView` | Lista de productos |
| `/<id>/` | `DetailView` | Detalle de un producto |
| `/crear/` | `CreateView` | Formulario para crear |
| `/<id>/editar/` | `UpdateView` | Formulario para editar |
| `/<id>/eliminar/` | `DeleteView` | Confirmación para eliminar |

El modelo `ProductModel` tiene título, precio, descripción, vendedor, color y medidas.

## Cómo ejecutarlo

```bash
python -m venv venv
venv\Scripts\activate        # en Linux o macOS: source venv/bin/activate
pip install django
python manage.py migrate
python manage.py runserver
```

Abre `http://127.0.0.1:8000/` y crea tu primer producto.

## Autor

Juan Carlos González Herrera · [LinkedIn](https://www.linkedin.com/in/juan-carlos-desarrollador-web) · [Portafolio](https://moremaster123.github.io)
