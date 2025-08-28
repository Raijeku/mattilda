# Frontend de Mattilda

Este es el frontend de Mattilda, construido con React y Vite. Proporciona la interfaz de usuario para gestionar escuelas, estudiantes y facturas.

---

## Cómo ejecutar

### 1. Instala las dependencias

```sh
cd frontend/app
npm install
```

### 2. Inicia el servidor de desarrollo

```sh
npm run dev
```

La app estará disponible en [http://localhost:5173](http://localhost:5173) (o el puerto que indique Vite).

---

## Proxy de la API

- El frontend está configurado para hacer proxy de las peticiones `/api` al backend (`http://127.0.0.1:8000`) mediante `vite.config.js`.
- Asegúrate de que el backend esté corriendo antes de iniciar el frontend.

---

## Archivos y carpetas importantes

- `src/pages/Schools.jsx`: Página principal para listar escuelas y sus detalles.
- `src/index.css`, `src/App.css`: Estilos globales y de componentes.
- `vite.config.js`: Configuración de Vite, incluyendo el proxy.
- `package.json`: Dependencias y scripts de NPM.

---

## Resolución de problemas

- Si ves errores de CORS o proxy, revisa que el backend esté en la dirección correcta.
- Para problemas de estilos o layout, revisa `index.css` y