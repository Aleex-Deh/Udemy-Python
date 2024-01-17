from coche import Coche

carro = Coche("Negro", "Reanult", "Clio", "150", "200", "2")
carro1 = Coche("Blanco", "Ferrari", "Aventador", "250", "300", "2")
carro2 = Coche("Amarillo", "Seat", "Ibiza", "100", "200", "4")
carro3 = Coche("Negro", "Reanult", "Clio", "150", "200", "4")

print(carro.getInfo())
print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())

# Detectar tipado
if type(carro3) == Coche:
    print ("Es un objeto correcto")
else:
    print("No es un objeto")
    
    
# Visibilidad
print(carro.soy_publico)
"""Lo comento ya que da error, es normal, ya que hemos definido una variable privada en la otra clase,
mediante 2 barras bajas consecutivas (__hola) se declara la variable hola como privada, si ya la 
quisieramos sacar a pública le hariamos un get con un return dentro """
#print(carro.__soy_privado)