import sys

fInput = open('input.in','r')
resultado=[]
contadorDeCases = 0
contadorNuevo = 0
for line in fInput:
    if contadorNuevo==0:
        contadorNuevo+=1
    else:    
        resultado = []
        contador = 0
        for char in line:
            if (len(resultado)==0):
                resultado.append(char)
            else:
                if(char<resultado[0]):
                    resultado.append(char)
                else:
                    resultado.insert(0,char)
            contador +=1
        f = open('output.txt','w')
        sres = "Case #" + str(contadorDeCases+1)+": "

        for letra in resultado:
            if (letra == '\n'):
                break
            else:    
                sres = sres + letra
    #f.write(sres)
        print sres
        contadorDeCases +=1