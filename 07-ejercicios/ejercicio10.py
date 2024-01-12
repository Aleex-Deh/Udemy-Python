"""
Ejercicio 10
Script que pida la nota de 15 alumnas y saca por pantalla cuantos han aprobado  cuantos han suspendido"""

contador = 0
aprobados = 0
suspendidos = 0
nota_alumnos = 0

for contador in range(0,15):
    nota_alumnos = input ("Proporcione una notas numéricas , porfavor: ")
    print (nota_alumnos)
    contador = contador + 1
    if int(nota_alumnos) < 5:
        suspendidos = suspendidos + 1
    else :
        aprobados = aprobados + 1
print(f"El recuento final indica que ha habido {aprobados} aprobados, pero {suspendidos} han suspendido")