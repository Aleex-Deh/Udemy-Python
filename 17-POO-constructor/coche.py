class Coche:
    # Esto son los atributos, son características del coche
    color = "rojo"    
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2
    
    soy_publico = "Soy un atributo público"
    __soy_privado = "Soy un atributo privado"
    
    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas
    
    # Métodos, son acciones que hace el objeto (coche) (funciones).
    def acelerar(self):
        self.velocidad += 1
    
    def frenar(self):
        self.velocidad -= 1
        
    def setVelocidad(self, velocidad):
        self.velocidad = velocidad
    
    def getVelocidad(self):
        return self.velocidad

    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color
    
    def setModelo(self, modelo):
        self.modelo = modelo
    
    def getModelo(self):
        return self.modelo
    
    def setMarca(self, marca):
        self.marca = marca
        
    def getMarca(self):
        return self.marca
    
    def getInfo(self):
        info = " \n### Datos del vehiculo ####"
        info += "\n Color: " + self.getColor()
        info += "\n MArca: " + self.getMarca()
        info += "\n Modelo: " + self.getModelo()
        info += "\n Velocidad: " + str(self.getVelocidad())
        return info