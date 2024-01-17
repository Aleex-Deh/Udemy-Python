"""
HERENCIA
Es la posibilidad de compartir atributos y métodos entre clases.
Y que diferentes clases hereden de otras            """

class Persona:
   
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def getNombre(self):
        return self.nombre
   
    
    
    def setApellidos(self, apellidos):
        self.apellidos = apellidos
        
    def getApellidos(self):
        return self.apellidos
   
   
    
    def setAltura(self, altura):
        self.altura = altura
        
    def getAltura(self):
        return self.altura
   
   
    
    def setEdad(self, edad):
        self.edad = edad
        
    def getEdad(self):
        return self.edad
    
    
    def hablar(self):
        return "Hola"
    
    def caminar(self):
        return "Andando"
    
    def dormir(self):
        return "Durmiendo ...."
    
    
""" Creo una nueva clase que herede lo de la clase padre (Persona), esto se hace
abriendo parentesis y poniendo su clase a heredar
"""
class Informatico(Persona):
    """
    lenguajes
    experiencas
    """
    def __init__(self):
        self.lenguajes = "HTML, CSS, JavaScript, PHP"
        self.experiencia = 5
        
    def getLenguajes(self):
        return self.lenguajes
    
    def aprender(self, lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes
    
    def programar(self):
        return "Programando ..."
    
    def repararPC(self):
        return "Reparando PC"
    
    
class TecnicoRedes(Informatico):
    def __init__(self):
        self.auditarRedes = "experto"
        self.experiencia = 5
        
    def auditoria(self):
        return "Auditando red"