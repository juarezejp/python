class Persona():
    def __init__(self, nombre, edad, residencia):
        self.nombre = nombre
        self.edad = edad
        self.residencia = residencia

    def estado(self):
        print("Nombre: ",self.nombre,
              "\nEdad: ",self.edad,
              "\nResidencia: ",self.residencia)

class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombre, edad, residencia):
        super().__init__(nombre, edad, residencia)
        self.salario = salario
        self.antiguedad = antiguedad
    
    def descripcion(self):
        super().estado()#llama a la clase padre
        print("salario: ", self.salario,
                "\nAntiguiedad: ", self.antiguedad)

emp = Empleado(300,5,"Edward", 25,"Mexico")
emp.descripcion()
print("emp es instancia de Empleado ",isinstance(emp,Empleado))

per = Persona(300,25,"MExico")
per.estado()
print(isinstance("per es instancia de Empleado ",per,Empleado))

