from io import open

#creacion de archivo externo
#W write 
#R Read
#A Append
archivo = open("fichero01.txt","w")
frase = "Feliz. \nhola"
archivo.write(frase)
archivo.close()


#lectura de archivos externos
archivo2 = open("fichero02.txt","r")
texto = archivo2.read()
archivo2.close()
print(texto)

#Agregar linea de texto
archivo2 = open("fichero02.txt", "a")
texto = "hola"
archivo2.write("\n"+texto)
archivo2.close()

#transformar lineas de texto a lista
archivo2 = open("fichero02.txt","r")
listalineas = archivo2.readlines()
archivo2.close()
print(listalineas)
print(listalineas[0])

