from io import open

#lectura de archivos externos segunda forma
archivo = open("fichero02.txt","r")
print(archivo.read())
archivo.seek(0) #Manda el puntero a la primera posicion
print(archivo.read())
archivo.seek(0)
print(archivo.read())
archivo.seek(2) #Manda el puntero al poscion de la cadena
print(archivo.read())
archivo.seek(0)
print(archivo.read(3)+"\n") #leer desde posicion especifica
archivo.seek(0)
archivo = open("fichero02.txt","r")
archivo.seek(len(archivo.readline()))
print(archivo.read()) #leer a partir del final del primer parrafo




