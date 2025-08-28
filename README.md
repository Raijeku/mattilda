# Mattilda

Mattilda es una aplicación full-stack para la gestión de escuelas, estudiantes y facturas. Incluye un backend FastAPI con SQLModel y un frontend React con Vite.

---

## Estructura del Proyecto

```
mattilda/
│
├── backend/      # Backend FastAPI + SQLModel
├── frontend/     # Frontend React + Vite
└── README.md     # Este archivo
```

---

## Cómo ejecutar el proyecto

### 1. Clona el repositorio

```sh
git clone https://github.com/Raijeku/mattilda.git
cd mattilda
```

### 2. Configura el backend

Consulta [backend/README.md](backend/README.md) para instrucciones detalladas.

### 3. Configura el frontend

Consulta [frontend/README.md](frontend/README.md) para instrucciones detalladas.

---

## Archivos importantes

- `backend/`: Código backend (API, modelos, base de datos, tests).
- `frontend/`: Código frontend (componentes React, estilos).
- `.gitignore`: Ignora archivos de entorno, node_modules, etc.

---

## Consejos de desarrollo

- Inicia primero el backend antes que el frontend para que funcione el proxy de la API.
- Usa terminales separadas para backend y frontend.
- Ejecuta los tests desde la carpeta `backend` para evitar problemas de imports.