import mysql.connector

def conectar():
        
    # Me conectoa mi base de datos ya creada, el el archivo basedatos.sql esta ahí todo
    database = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "master_python",
        port = 3306
    )

    # Buffered=True, permite hacer muchas consultas sin que de errores
    cursor = database.cursor(buffered=True)
    return[database, cursor]