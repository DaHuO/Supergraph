from __future__ import print_function

entrada = open("in.txt", "r+")
salida = open("out.txt", "r+")

cases = int(entrada.readline())

for k in range(1, cases+1):
    cont=0
    aux=0
    estados= list(entrada.readline()[:-1])
    entro = False
    veces = 0
    #print(estados)
    if '-' not in estados:
        #print("Case #"+str(k)+": "+str(cont))
        salida.write("Case #"+str(k)+": "+str(cont)+"\n")
    while ('-'  in estados):
        ##Calcular hasta donde estan los +
        entro=True
        veces = veces+1
        #print(estados)
        if estados[0] is '+' :
            for i  in estados:
                if i is '+':
                    aux= aux+1
                else:
                    break
            for j in range(0,aux):
                estados.pop(0)
            for j in range(0,aux):
                estados.insert(0,'-')
            cont = cont+1
            aux=0
        elif estados[0] is '-' :
            for i  in estados:
                if i is '-':
                    aux= aux+1
                else:
                    break
            for j in range(0,aux):
                estados.pop(0)
            for j in range(0,aux):
                estados.insert(0,'+')
            cont = cont+1
            aux=0


    if(entro is True):
        #print("Case #"+str(k)+": "+str(cont))
        salida.write("Case #"+str(k)+": "+str(cont)+"\n")
