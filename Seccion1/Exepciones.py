def suma(n1,n2):
    return n1+n2

def resta(n1,n2):
    return n1-n2

def multiplicacion(n1,n2):
    return n1*n2

def division(n1,n2):
    #divisionentre cero
    try:  
        return n1/n2
    except ZeroDivisionError:
        print("No es divisible entre 0")
        return "Operacion fallida."

a = 1
b = 2
c = 0
#d = "d"

print(suma(a,b))
print(resta(a,b))
print(multiplicacion(a,b))
print(division(a,c))

#tipo de datos error
try:
    d = "d"
    print(suma(a,d))
except TypeError:
    print("ingrese datos validos")

#Excepcion de entrada valores
try:
    a = int(input("Ingresa un numero: "))
except ValueError as e:
    print("valor invalido...{}".format(e))
    
'''
try:
    print(suma(a,d))
except Exception as e:
    raise e
'''
