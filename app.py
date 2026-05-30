# app.py - Backend TechStore S.A.C. con Arquitectura MVC
import os
import sys
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

# Asegurar que el directorio raíz del proyecto sea el primero en la lista de búsqueda.
# Esto evita conflictos si tienes instalada una librería global llamada 'routes'.
root_path = os.path.dirname(os.path.abspath(__file__))
if root_path not in sys.path:
    sys.path.insert(0, root_path)

# Cargar variables de entorno desde .env
load_dotenv()

from config import Config
from models.db_helpers import init_db
from controllers.auth_controller import auth_bp
from controllers.product_controller import product_bp
from controllers.web_controller import web_bp

def create_app():
    """Crea y configura la aplicación Flask."""
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', app.config['SECRET_KEY'])
    app.config['DATABASE_PATH'] = os.getenv('DATABASE_PATH', app.config['DATABASE_PATH'])
    app.secret_key = app.config['SECRET_KEY']

    # Habilitar CORS para permitir peticiones desde Flutter
    CORS(app)

    # Registrar Blueprints (las rutas ya incluyen el prefijo '/api' cuando aplica)
    app.register_blueprint(auth_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(web_bp)

    return app

app = create_app()
init_db()

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=os.getenv('FLASK_DEBUG', 'True') == 'True', host='0.0.0.0', port=port)