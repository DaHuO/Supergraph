def listaDigitos(x,digitos):
    while x > 0:
        digitos.add(x%10)
        x = x//10
    return digitos

def procesa(numeroInicial):
    listaAparecida = set()
    counter = 0
    while len(listaAparecida.intersection(listaNumeros))<10:
        counter = counter + 1
        listaDigitos(numeroInicial*counter,listaAparecida)
    return numeroInicial*counter

listaNumeros = set()
for i in range(10):
    listaNumeros.add(i)

#cargamos los casos
f = open('A-large.in', 'r')
o = open('testL.out',mode = 'w')

nCases = int(f.readline())

for i in range(1,nCases+1):
    initN = int(f.readline())
    if initN == 0:
        dd = "INSOMNIA"
    else:
        dd = str(procesa(initN))

    o.write("Case #"+str(i)+": "+dd+"\n")
o.close()
