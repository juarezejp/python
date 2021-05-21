class Computadora():
    def __init__(self):
        self.marca = "Lenovo"
        self.procesador = "AMD"
        self.mouse = 1
        self.teclado = 1
        self.suspendido = False

    def ejecucion(self, suspencion):
        self.suspendido=suspencion
    
    def estado(self):
        if(self.suspendido):
            print("El equipo esta suspendido. ")
        else:
            print("El equipo esta en ejecucion")

pc = Computadora()
print("Marca: ",pc.marca)
print("Procesador: ",pc.procesador)
print("Mouse: ",pc.mouse)
print("Teclado: ", pc.teclado)
pc.ejecucion(True)
print(pc.estado())


pc2 = Computadora()
print("Marca: ",pc2.marca)
print("Procesador: ",pc2.procesador)
print("Mouse: ",pc2.mouse)
print("Teclado: ", pc2.teclado)
pc2.ejecucion(False)
print(pc2.estado())