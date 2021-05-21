def suma(n1,n2):
    print(n1+n2)

def resta(n1,n2):
    print(n1-n2)

def multiplicacion(n1,n2):
    print(n1*n2)

def division(n1,n2):
    #divisionentre cero
    try:  
        print(n1/n2)
    except ZeroDivisionError:
        print("No es divisible entre 0")
        print("Operacion fallida.")