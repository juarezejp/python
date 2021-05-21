import pickle

carreras = ["IS","Medicina","Administracion","contabilidad","Arqui"]
fichero = open("carreras","wb") #escritura en binario
pickle.dump(carreras,fichero)
fichero.close()
#abrir fichero en binario.
fichero = open("carreras","rb")
lista = pickle.load(fichero)
print(lista)



