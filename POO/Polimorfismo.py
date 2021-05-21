class Gerente():

    def marcacion(self):
        print("Marca asistencia una vez.")


class Subgerente():
    def marcacion(self):
        print("Marca asistencia dos veces.")


class JefeArea():
    def marcacion(self):
        print("Marca asistencia tres veces.")

class Asistente():
    def marcacion(self):
        print("Marca asistencia cuatro veces y firma.")


def marcacionTrabajador(trabajador):
    trabajador.marcacion()

mTrabajador = Subgerente()
marcacionTrabajador(mTrabajador)

mTrabajador2 = Gerente()
marcacionTrabajador(mTrabajador2)

mTrabajador3 = JefeArea()
marcacionTrabajador(mTrabajador3)

mTrabajador4 = Asistente()
marcacionTrabajador(mTrabajador4)
