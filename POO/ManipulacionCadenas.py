nombre = "Eliadio JP"
nombre2 = "eladioJP"
numletra = "33k"
numeroS = "5555"

#devuelve en minusculas la cadena
print(nombre.lower())
#devuelve en mayusculas la cadena
print(nombre.upper())
#devuelve la cadena el primer caracter en mayuscula
print(nombre2.capitalize())
#devuelve true si la cadena es digitos
print (numletra.isdigit())
print (numeroS.isdigit())
#devuelve el indice minimo
print(nombre.find("da",0,6)) #-1 si no lo encuentra
print(nombre.find("i",0,6)) #indice del primer caracter
#devuelve el indice maximo en donde se encuentra la subcadena
print(nombre.rfind("i"))
print(nombre.rfind("i", 1, 4))
#devuelve verdadero si todos los caracteres son alfanumericos
print(nombre.isalnum())
print(numletra.isalnum())
print(numeroS.isalnum())
#devuelve true si todos los caracteres son alfabeticos o hay almenos un caracter
print(nombre.isalpha()) #regresa falso por que hay espacio en blanco
print(nombre2.isalpha())
print(numeroS.isalpha())
#devuelve lista de las palabras de la cadena
print(nombre.split())
#reemplaza una copia de la cadena en la que se sustitulle old por new
print(nombre.replace("i","A"))
print(nombre.replace("i","A",1)) #1 cantidad de veces a remplazar



