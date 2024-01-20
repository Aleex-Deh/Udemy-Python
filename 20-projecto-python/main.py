"""
Proyecto Python con Mysql
- Abrir asistente
- Login o registro
- Si elegimos registro, creará un usario en la bbdd
- Si elegimos login, identificará al usuario y nos preguntará
- Crear nota, mostrar nota, borrarlas
"""
from usuarios import acciones

print("""
Acciones disponibles :
- registro
- login
""")

# Saco la accion del pequete ususarios, del modulo acciones.
accion = input("\nQue opcion quere hacer: ")
hazEl = acciones.Acciones()

if accion == "registro":
    hazEl.registro()
elif accion == "login":
    hazEl.login()