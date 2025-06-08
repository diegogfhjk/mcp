import os
import sqlite3
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DB_PATH = os.path.join(BASE_DIR, "inventory.db")

def init_db():
    print(f"[InventarioDB] [debug] Inicializando DB en: {DB_PATH}", file=sys.stderr)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        categoria TEXT,
        cantidad INTEGER,
        precio REAL
    )
    """)
    conn.commit()
    conn.close()