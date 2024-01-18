import mysql.connector

#Conexion
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd= "",
    database= "master_python"
)
#Defino el cursor, para poder hacer consultas. 
#EL biffered=True se pone para caundjo ejecturemos muchas onsultas no no de fallos
cursor = database.cursor(buffered=True)
"""
# Creo la BD mediante la ayuda del cursor
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

# Enseño las tablas mediante la ayuda del cursor
cursor.execute("SHOW DATABASES")
for bd in cursor:
    print(bd)
"""

# Creo nueva table
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
id int(10) auto_increment not null,
marca varchar(40) not null,
modelo varchar(40) not null,
CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")

# Enseño la nueva tabla
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)
    
    
"""
# Insertar registros
cursor.execute("INSERT INTO vehiculos VALUES(null, 'opel', 'Asta', 18500)")
#Lo guardo, es database, porque el commit solo esta en la base de datos y no en el cursor.
database.commit()
"""

# Muestro lo que quiero mediante el select
cursor.execute("SELECT * FROM vehiculos")
result = cursor.fetchall()
for coche in result:
    print(coche)
    
# Eliminar 
cursor.execute("DELETE FROM vehiculos WHERE marca = 'Renault' ")
# Guardo el registro
database.commit()

# Actualizar /modificar un registro ya escrito
cursor.execute("UPDATE vehiculos SET modelo='Lamborgini' WHERE marca='Asta'")
database.commit()