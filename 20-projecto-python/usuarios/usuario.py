import datetime
import hashlib # Para cifrar la contraseña del usuario
import usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Usuario:
    
    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password
        
# No uso getter and setter, ya que en este caso no es específico y solo alargaria el codigo.

# Pongo el %s, ya que el parametro se le asignará mas tarde, ya que los parámetros estarán dentro de una tupla.
    def registrar(self):  
        fecha = datetime.datetime.now()
        
        # Cifro la contraseña aqui
        cifrado = hashlib.sha256()
        
        """ EL update, me permite asignarle un parametro a cifrar en bytes, pero para pasarselo a bytes necesito el .encode """
        cifrado.update(self.password.encode('utf8'))   
        
        sql = "INSERT INTO usuario VALUES(null, %s, %s, %s, %s, %s)"    
        """ Aqui uso como un checksum, mediante el .hexdigest me corrobora el string hexadecimla, y si coincide es q es correcto"""
        usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha)
        
        
        try:
            # Le asigno la consulta que quiero (sql), y los datos a introducir (usario)
            cursor.execute(sql, usuario)       
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]
            
        return  result


    def identificar(self): 
        sql = "SELECT * FROM usuario WHERE email = %s AND password = %s"
        
        cifrado = hashlib.sha256()

        """ EL update, me permite asignarle un parametro a cifrar en bytes, pero para pasarselo a bytes necesito el .encode """
        cifrado.update(self.password.encode('utf8')) 
        
        # Datos para la consulta
        usuario = (self.email, cifrado.hexdigest())
        
        cursor.execute(sql, usuario)
        result = cursor.fetchone()
        return result