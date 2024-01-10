my_texto = "Master"
My_texto2 =  "en Python"

#Texto concatenado normal
textos_unidos = my_texto + " " + My_texto2
print (textos_unidos)

#Texto concatenado pero con salto de linea
textos_unidos = my_texto + " \n" + My_texto2
print (textos_unidos)

#Texto concatenado pero con una tabulación
textos_unidos = my_texto + " \t" + My_texto2
print (textos_unidos)


#Texto concatenado, lo que esta detras de la \r se elimina
textos_unidos = my_texto + " \r" + My_texto2
print (textos_unidos)