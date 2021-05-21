class Computadora():
    def __init__(self):
        self.__marca = "Lenovo"
        self.__procesador = "AMD"
        self.__mouse = 1
        self.__teclado = 1
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


pc = Computadora()
pc.ejecucion(True)
print(pc.estado())
print("__________________________")

pc2 = Computadora()
pc2.ejecucion(False)
print(pc2.estado())