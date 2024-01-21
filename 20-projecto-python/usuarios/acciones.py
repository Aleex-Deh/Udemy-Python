import usuarios.usuario as modelo       #Le voy a nombrar como modelo

class Acciones:
    
    def registro(self):
        
        print("\nRegistrandote en el sistema")
        nombre = input("Cual es tu nombre: ")
        apellido = input("Cuales son tus apellidos: ")
        email = input("Cual es tu email: ")
        password = input("Cual es tu contraseña: ") 
        
        usuario = modelo.Usuario(nombre, apellido, email, password)
        registro = usuario.registrar()
        
        if registro[0] >=1:
            print(f"\nCorrecto, {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("\nNo te has registrado correctamente")
        
        
    def login(self):
        
        print("\nIdentificandote en el sistema")
        try:
                
            email = input("Introduzca su email: ")
            password = input("Introduzca su contraseña: ")
            
            usuario = modelo.Usuario('', '', email, password)
            login = usuario.identificar()
            
            if email == login[3]:
                print(f"\n Bienvenido {login[1]}, te has registrado en el {login[5]}")
        except Exception as e:
            print(f"Login incorrecto, intentalo mas tarde")