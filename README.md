git add .
git commit -m "Initial commit: prepare repo for Render"
git branch -M main
git push -u origin main
# backend_flask / TechStore Backend (Flask)

Pequeña API/Backend en Flask con arquitectura MVC para TechStore S.A.C.

Preparado para desplegar en Render.

Pasos rápidos para subir a GitHub y desplegar en Render:

1. Inicializar git local (ya preparado en este repo):

```bash
git init
git add .
git commit -m "Initial commit: prepare repo for Render"
```

2. Crear repo en GitHub y empujar (opción con `gh` CLI):

```bash
# Reemplaza <OWNER> y <REPO_NAME>
gh repo create <OWNER>/<REPO_NAME> --public --source=. --remote=origin --push
```

Si no tienes `gh`, crea el repo en GitHub vía web y luego:

```bash
git remote add origin https://github.com/<OWNER>/<REPO_NAME>.git
git branch -M main
git push -u origin main
```

3. Conectar en Render:

- Ve a https://dashboard.render.com
- Crea un nuevo Web Service y conéctalo al repo de GitHub que creaste.
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app:app -b 0.0.0.0:$PORT`
- Define variables de entorno en la sección Environment (ej.: `SECRET_KEY`).

Notas importantes:
- `database.db` es SQLite y estará en el filesystem del servicio; para datos persistentes en producción usa una base de datos gestionada y actualiza `models/db_helpers.py`.
- Añade secretos (SECRET_KEY, etc.) desde el panel de Render en lugar de subirlos al repo.

## BACKEND_FLASK - Arquitectura MVC

Proyecto backend desarrollado con **Flask**, **SQLite** y **Flask-CORS**, reorganizado bajo el patrón arquitectónico **MVC**.

### Estructura del proyecto

```text
BACKEND_FLASK/
├── app.py
├── config.py
├── requirements.txt
├── database.db
├── controllers/
│   ├── __init__.py
│   ├── auth_controller.py
│   ├── product_controller.py
│   └── web_controller.py
├── models/
│   ├── __init__.py
│   ├── db.py
│   ├── user_model.py
│   └── product_model.py
├── views/
│   └── templates/
│       ├── login.html
│       ├── principal.html
│       └── productos.html
└── static/
    └── style.css
```

### Instalación

```bash
cd BACKEND_FLASK
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

En macOS/Linux:

```bash
source venv/bin/activate
python app.py
```

### Usuario de prueba

```text
usuario: admin
clave: admin123
```

### Endpoints REST para Flutter

```text
POST    /api/login
GET     /api/productos
GET     /api/productos/buscar?q=laptop
POST    /api/productos
PUT     /api/productos/<id>
DELETE  /api/productos/<id>
```

### Rutas web

```text
GET/POST / 
GET      /principal
GET/POST /productos-web
GET      /salir
```

### Recomendación de seguridad

Este ejemplo conserva contraseñas en texto plano porque corresponde a un laboratorio académico.
En producción, se debe aplicar hashing de contraseñas con herramientas como `werkzeug.security`.

