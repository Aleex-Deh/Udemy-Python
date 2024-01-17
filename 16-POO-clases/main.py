"""
PROGRAMACIÓN ORIENTADA A OBJETOS        (POO    o     OOP)
"""
# Definimos la clase. Una clase es el molde para crear objetos sobre ese tema/clase
class Coche:
    # Esto son los atributos, son características del coche
    color = "rojo"    
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2
    
    # Métodos, son acciones que hace el objeto (coche) (funciones).
    def acelerar(self):
        self.velocidad += 1
    
    def frenar(self):
        self.velocidad -= 1
    
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


# Crear objeto / instanciar a la clase
coche = Coche()

# Usando getter y setter
# Getter: Método que devuelve el valor actual de un atributo. Da acceso de solo lectura.
# Setter: Método que establece un nuevo valor para un atributo. Da acceso de escritura y asigna los valores.


coche.setColor("amarillo")
coche.setModelo("murcielago")

# Imprimir información sobre el coche
print("Marca:", coche.marca)
print("Modelo:", coche.getModelo())
print("Color:", coche.getColor())

# Imprimir velocidad actual y acelerar
print("Velocidad actual:", coche.velocidad)
coche.acelerar()
coche.acelerar()
coche.acelerar()
print(f"Velocidad nueva es de {coche.velocidad}")

#Crear mas objetos.     Simplemente enumerando o cambiando la variable que sea igual a la clase
coche2 = Coche()
print(coche2.getColor())