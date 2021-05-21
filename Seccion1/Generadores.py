def listPares(limite):
    num=1
    miLista=[]
    while(num<limite):
        miLista.append(num*2)
        num+=1
    return miLista

print (listPares(8))

#generador
def listPares2(limite):
    num=1
    while(num<limite):
        yield(num*2)
        num+=1

returnPares = listPares2(8)
for i in returnPares:
    print (i)
#mostrar elementos especificos
returnPares2 = listPares2(8)
print(next(returnPares2))
print(next(returnPares2))
print(next(returnPares2))
print(next(returnPares2))
print(next(returnPares2))
print(next(returnPares2))
print(next(returnPares2))