def evaluacion(nota):
    estado = "promovido"
    if nota < 11:
        estado = "Sustituirlo"
    return estado

print(evaluacion(10))
print(evaluacion(11))

sueldoGerente = 1000
sueldoJefeArea = 950
sueldoAsistente = 900
sueldoTecnico = 850
sueldoPracticante = 800

def comparacion(sueldo1, sueldo2):
    if(sueldo1 > sueldo2) :
        return "sueldo 1 es mayor"
    else :
        return "sueldo 2 es mayor"

print(comparacion(sueldoGerente,sueldoJefeArea))
print(comparacion(sueldoPracticante,sueldoGerente))



def comparacion2(promedio, edad, inscrito):
    if(promedio >= 6):
        if(edad >= 18):
            if(inscrito == "inscrito"):
                return "Si cumple"
            else:
                return "no cumple inscrito"
        else:
            return "no cumple edad"
    else:
        return "no cumple promedio"

print(comparacion2(6,17,"inscrito"))