class Carro():
    #Atributos
    marca="Audi"
    longitud=2.5
    ruedas=4
    motor=2.5
    color="negro"
    modelo="Q5"

    #Propiedades
    arrancar=False
    frenar=False

    #Metodos
    def en_marcha(self):
        self.arrancar=True
    
    def estado(self):
        if(self.arrancar):
            return "El auto esta en marcha"
        else:
            return "El auto esta detenido"

auto = Carro()
print("Marca del auto ",auto.marca)
print("longitud del auto ",auto.longitud)
print("ruedas del auto ",auto.ruedas)
print("color del auto ",auto.color)
print("modelo del auto ",auto.modelo)

#llamada a metodos
print(auto.estado())
auto.en_marcha()
print(auto.estado())
