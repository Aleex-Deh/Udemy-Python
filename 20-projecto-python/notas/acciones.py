import notas.nota as modelo

class Acciones:
    
    def crear(self, usuario):
        print(f"Hola {usuario[1]}, \ncreando una nueva nota ...")
        
        titulo = input("\nIntroduce el titulo de tu nota: ")
        descripcion = input("Introduce el contenido de tu nota: ")
        
        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()
        
        if guardar[0] >= 1:
            print(f"\nPerfecto, has guardado la nota: {nota.titulo}")
        else :
            print(f"No se ha podido guardar la nota, lo sentimos {usuario[1]}")
            
        
    def mostrar(self, usuario):
        print(f"\n De acuerdo {usuario[1]}, aqui tiene sus notas: ")
        nota = modelo.Nota(usuario[0])
        notas = nota.listar()
        
        for nota in notas:
            print("################################")
            print(nota[2])
            print(nota[3])
            print("################################\n")


    def borrar(self, usuario):
        print(f"\n De acuerdo, {usuario[1]}. Vamos a a borrar notas")
        
        titulo = input("Introduce el titulo de la nota que deseas eliminar: ")
        
        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar(usuario[0], titulo)
        
        if eliminar[0] >= 1:
            print(f"Hemos borrado la nota : {nota.titulo}")
        else:
            print("No se ha podido borrar la nota, intentelo mas tarde")