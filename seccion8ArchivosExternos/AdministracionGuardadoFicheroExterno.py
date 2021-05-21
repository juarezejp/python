import pickle

class Computadora():

    def __init__(self, __marca,__procesador,__mouse,__teclado):
        self.__marca = __marca
        self.__procesador = __procesador
        self.__mouse = __mouse
        self.__teclado = __teclado
        print("se ha creado un nuevo equipo de marca ",self.__marca)

    #convertir en cadena de texto
    def __str__(self):
        return "{} {} {} {}".format(self.__marca,self.__procesador,self.__mouse,self.__teclado)

class ListaPCs:
    pcs = []
    
    def __init__(self):
        ListaPCs = open("Ordenadores","ab+") #agregar informacion binaria
        ListaPCs.seek(0)
        try:
            self.pcs = pickle.load(ListaPCs)
            print("Se cargaron {} computadoras en el fichero ".format(len(self.pcs)))
        except:
            print("El fichero no contiene nada.")
        finally:
            ListaPCs.close()
            del(ListaPCs)

    def agregarPCs(self, pc):
        self.pcs.append(pc)
        self.guardarPCs()
    
    def mostrarPCs(self):
        for pc in self.pcs:
            print(pc)

    def guardarPCs(self):
        ListaPCs = open("Ordenadores","wb")
        pickle.dump(self.pcs,ListaPCs)
        ListaPCs.close()
        del(ListaPCs)
    
    def mostrarInfoFichero(self):
        print("La informacion del fichero es ")
        for pc in self.pcs:
            print(pc)


miPC = ListaPCs()
pc = Computadora("Lenovo","AMD","Microsoft","Dell")
miPC.agregarPCs(pc)
miPC.mostrarPCs()
miPC.mostrarInfoFichero()





