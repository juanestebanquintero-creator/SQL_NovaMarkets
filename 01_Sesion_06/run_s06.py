import sqlite3
import os

db_path = "01_Base_Datos_S06.db"
sql_path = "03_Laboratorio_S06.sql"

if os.path.exists(db_path):
    os.remove(db_path)
    print(f"Borrando {db_path} existente.")

print(f"Creando la base de datos {db_path}...")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print(f"Ejecutando script {sql_path}...")
with open(sql_path, "r", encoding="utf-8") as f:
    sql_script = f.read()

try:
    cursor.executescript(sql_script)
    print("¡Script ejecutado con éxito!")
except Exception as e:
    print(f"Error al ejecutar el script: {e}")

conn.commit()
conn.close()
print("Proceso finalizado.")
