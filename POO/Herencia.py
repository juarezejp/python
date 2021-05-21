class Persona():
    def __init__(self, nombre, apellido, sexo):
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.hablar = False
    
    def hablar(self):
        self.hablar = True
    
    def estado(self):
        print("Nombre: ",self.nombre,
              "\nApellido : ",self.apellido,
              "\nSexo : ",self.sexo,
              "\nHablar : ",self.hablar)
    
class Supervisor(Persona):
    objetivo = ""
    
    def objetivos(self):
        self.objetivo = "Cumplir Metas"
    
    def estado(self):
        print("Nombre: ",self.nombre,
              "\nApellido : ",self.apellido,
              "\nSexo : ",self.sexo,
              "\nHablar : ",self.hablar,
              "\nObjetivo : ",self.objetivo)

class Obrero(Persona):
    manejarMaquina = ""
    
    def manejar(self):
        self.manejarMaquina = "Manejar Maquina"
    
    def estado(self):
        print("Nombre: ",self.nombre,
              "\nApellido : ",self.apellido,
              "\nSexo : ",self.sexo,
              "\nHablar : ",self.hablar,
              "\nObjetivo : ",self.manejarMaquina)

print("_____Datos Supervisor_____")
miSupervisor = Supervisor("Juan", "Gonzales", "Masculino")
miSupervisor.objetivos()
miSupervisor.estado()
print("_____Datos Obrero_____")
miObrero = Obrero("Pedro", "Gonzales", "Masculino")
miObrero.manejar()
miObrero.estado()


