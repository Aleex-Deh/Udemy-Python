#Importo el darchivo del cual saco las clase que quiero
import clases


persona = clases.Persona()
#Defino la informacion que le quiero pasar a las funciones
persona.setNombre("Alex")
persona.setApellidos("Dehesa Delgado")
persona.setAltura("190")
persona.setEdad("18 años")


print(f"La persona es {persona.getNombre()} {persona.getApellidos()}        \n ########## \n")
print(persona.hablar())
print(persona.dormir())

#Aqui dejo 2 ejemplos de como se usaria de forma correcta las herencias
informatico = clases.Informatico()
informatico.setNombre("Paco")
informatico.setApellidos("Garcia DeJuan")
print(f"La persona es {informatico.getNombre()} {informatico.getApellidos()}        \n ########## \n")
print(informatico.getLenguajes())

tecnico = clases.TecnicoRedes()
tecnico.setNombre("Manolo")
print(tecnico.auditarRedes, tecnico.getNombre(), informatico.getLenguajes())