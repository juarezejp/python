a = 0
while (a<=5):
    print(a)
    a += 1


for a in [1,10,3,4,5,6]:
    print("hola{}".format(a))

for a in ['juan','jose',12,10.3]:
    print(a)

cont = 0
for a in 'juarez@gmail.com':
    if(a =='@' or a == '.'):
        cont += 1
if cont == 2:
    print("si cumple email")
else:
    print("no cumple")


for i in range(10):
    print("i")

for i in range(-2, 5, 1):#donde empieza, donde termina, incrimento
    print(i)

for i in range(4, 0, -1):#donde empieza, donde termina, incrimento
    print(i)
