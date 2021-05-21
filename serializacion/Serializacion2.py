import pickle

class Computadora():

    def __init__(self, __marca,__procesador,__mouse,__teclado):
        self.__marca = __marca
        self.__procesador = __procesador
        self.__mouse = __mouse
        self.__teclado = __teclado

        self.__ejecutar = False

    def ejecucion(self, ejecuciones):
        self.__ejecutar = ejecuciones
    
    def estado(self):
        if(self.__ejecutar):
            update = self.__actualizacion_automatica()
        if(self.__ejecutar and update):
            print("El equipo esta en ejecucion.")
        else:
            print("El equipo esta suspendido.")

    def __actualizacion_automatica(self):
        print("El equipo  se esta actualizando...")
        self.servupdate = "Activado"
        if(self.servupdate == "Activado"):
            return True
        else:
            return False


pc1 = Computadora("Toshina","amd","Hp","Genius")
pc2 = Computadora("Lenovo","amd","Genius","Microsofth")
pc3 = Computadora("Sony","Intel","Lenovo","HP")

pc = [pc1,pc2,pc3]
fichero = open("EquipoTI","wb")
pickle.dump(pc, fichero)
fichero.close()
del(fichero) #cerrar memoria interna e eliminar de memoria
 #abrir fichero y mostrarlo
archivo = open("EquipoTI","rb")
pcs = pickle.load(archivo)
archivo.close()
for c in pcs:
    print(c.estado())

