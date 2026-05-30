import sqlite3
import os

# Obtenemos la ruta absoluta para evitar errores de "file not found"
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATABASE = os.getenv('DATABASE_PATH', os.path.join(BASE_DIR, 'database.db'))

def get_db_connection():
    conn = sqlite3.connect(DATABASE, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Crea las tablas e inserta datos iniciales si no existen."""
    conn = get_db_connection()
    cursor = conn.cursor()

    # Crear tabla usuario
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuario (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT    NOT NULL UNIQUE,
            password TEXT    NOT NULL,
            nombre   TEXT,
            activo   INTEGER DEFAULT 1
        )
    ''')

    # Crear tabla producto
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS producto (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo      TEXT    NOT NULL UNIQUE,
            nombre      TEXT    NOT NULL,
            categoria   TEXT    NOT NULL,
            precio      REAL    NOT NULL,
            stock       INTEGER DEFAULT 0,
            descripcion TEXT
        )
    ''')

    # Insertar datos iniciales si la tabla está vacía
    cursor.execute("SELECT COUNT(*) FROM usuario")
    if cursor.fetchone()[0] == 0:
        cursor.execute(
            "INSERT INTO usuario (username, password, nombre) VALUES (?,?,?)",
            ('admin', 'admin123', 'Administrador TechStore')
        )
        cursor.execute(
            "INSERT INTO usuario (username, password, nombre) VALUES (?,?,?)",
            ('vendedor1', 'pass123', 'Juan Pérez')
        )

    cursor.execute("SELECT COUNT(*) FROM producto")
    if cursor.fetchone()[0] == 0:
        productos = [
            ('PROD-001', 'Laptop HP Pavilion 15', 'Laptops', 2899.90, 10, 'Procesador Intel i5 12va generación'),
            ('PROD-002', 'Mouse Logitech MX Master', 'Periféricos', 189.90, 25, 'Mouse inalámbrico ergonómico'),
            ('PROD-003', 'Teclado Mecánico Redragon', 'Periféricos', 249.90, 15, 'Switches rojos, retroiluminado RGB'),
            ('PROD-004', 'Monitor Dell 24 FHD', 'Monitores', 799.90, 8, 'Pantalla IPS 1920x1080 75Hz'),
            ('PROD-005', 'Auriculares Sony WH-1000XM5', 'Audio', 1299.90, 12, 'Cancelación de ruido activa'),
            ('PROD-006', 'Smartphone Samsung Galaxy A54', 'Smartphones', 1199.90, 20, '6.4 pulgadas, 128GB, 5G'),
            ('PROD-007', 'Tablet iPad Air 5ta Gen', 'Tablets', 2999.90, 5, '10.9 pulgadas, M1 chip, WiFi'),
            ('PROD-008', 'SSD Kingston 1TB', 'Almacenamiento', 299.90, 30, 'SATA III, lectura 550 MB/s'),
        ]
        cursor.executemany(
            'INSERT INTO producto (codigo, nombre, categoria, precio, stock, descripcion) VALUES (?,?,?,?,?,?)',
            productos
        )

    conn.commit()
    conn.close()
    print('[DB] Base de datos inicializada correctamente bajo patrón MVC.')