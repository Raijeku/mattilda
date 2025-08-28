# Frontend de Mattilda

Frontend en React + Vite.

---

## Ejemplo visual

<div align="center">
  <img src="../images/escuelas.png" alt="Pantalla de escuelas" width="600"/>
</div>

---

## Cómo ejecutar

### Opción 1: Docker Compose

```sh
docker-compose up --build
```

### Opción 2: Manual

1. Instala dependencias:

   ```sh
   cd frontend/app
   npm install
   ```

2. Inicia el servidor de desarrollo:

   ```sh
   npm run dev
   ```

---

## Archivos importantes

- `src/pages/Schools.jsx`, `Students.jsx`, `Invoices.jsx`
- `vite.config.js`: Configuración de proxy.
- `images/`: Capturas de pantalla.

---

## Notas

- El frontend usa Bootstrap para el diseño.
- El proxy de la API está configurado en `vite.config.js`.