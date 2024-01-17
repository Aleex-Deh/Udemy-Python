"""
Sqlite.    
Es una sistema gestor de bases de datos ligero que vienen integrado dentro del lenguaje de python      """

#Importamos el modulo del gestor ligero de base de datos
import sqlite3

# Abrimos conexion. (se crea nuestra base de datos)
conexion = sqlite3.connect("pruebas.db")

# Creamos el cursor.   El cursor es el que nos permite ejecutar las cosultas de las bases de datps
cursor = conexion.cursor()

# Creamos la tabla.     Metemos los + para poder concatenar
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
"id INTEGER PRIMARY KEY AUTOINCREMENT NOT null, "+
"titulo VARCHAR(255), "+
"descripcion TEXT, "+
"precio int(255)"+
")")

# Insertar dato
cursor.execute("INSERT INTO productos VALUES (null, 'primer producto', 'Descripcion de mi producto', 550)")

# Listar datos existentes
producto = cursor.fetchone()
print(producto)

# Guardar cambios
conexion.commit()


# Cerramos conexion. Siempre hay que cerrar la conexion
conexion.close()

