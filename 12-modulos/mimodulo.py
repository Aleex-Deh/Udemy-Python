def holamundo(nombre):
    return f"Hola que tal estas, {nombre}"


def calculadora(numero1, numero2, basicos = False):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1 / numero2
    
    if basicos != False:
        cadena = ""
        cadena += "Suma : " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "Multiplicacion: " + str(multiplicacion)
        cadena += "\n"
        cadena += "Division: " + str(division)
        cadena += "\n"
    return cadena
