# Backend de Mattilda

Este es el backend de Mattilda, construido con FastAPI y SQLModel. Provee APIs REST para gestionar escuelas, estudiantes y facturas.

---

## Cómo ejecutar

### 1. Crea un entorno virtual

```sh
cd backend
python -m venv .env
```

### 2. Activa el entorno

- **Windows:**  
  `.\.env\Scripts\activate`
- **Linux/macOS:**  
  `source .env/bin/activate`

### 3. Instala las dependencias

```sh
pip install -r requirements.txt
```

### 4. Ejecuta el servidor

```sh
uvicorn app.main:app --reload
```

La API estará disponible en [http://localhost:8000](http://localhost:8000).

---

## Archivos y carpetas importantes

- `app/main.py`: Punto de entrada de FastAPI. Incluye routers y crea las tablas.
- `app/db.py`: Lógica de sesión y creación de base de datos.
- `app/core/settings.py`: Configuración (por ejemplo, URL de la base de datos).
- `app/models/`: Modelos SQLModel para `School`, `Student` e `Invoice`.
- `app/routes/`: Routers de FastAPI para cada recurso.
- `app/tests/`: Tests con Pytest para los endpoints.
- `requirements.txt`: Dependencias de Python.

---

## Ejecutar tests

Desde la carpeta `backend`:

```sh
pytest
```

---

## Notas

- El backend usa SQLModel (basado en SQLAlchemy) como ORM.
- Asegúrate de que tu base de datos esté configurada en `app/core/settings.py`.
- Todos los endpoints están documentados en `/docs` gracias a FastAPI.

---

## Resolución de problemas

- Si ves `ModuleNotFoundError: No module named 'app'`, asegúrate de ejecutar `uvicorn` desde la carpeta `backend`.
- Si tienes errores de base de datos, revisa que esté corriendo y la cadena de conexión sea correcta.