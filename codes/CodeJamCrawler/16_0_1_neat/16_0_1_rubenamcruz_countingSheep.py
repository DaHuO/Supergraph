#!/usr/bin/env python

N = int(raw_input())

i = 1
aux = range(0, 10)
numeros = []
for x in aux:
    numeros.append(str(x))

while i <= N:
    b = True
    T = int(raw_input())
    res = T
    j = 1
    digitos = set()
    while(b):
        inT = str(res)
        for x in inT:
            digitos.add(x)
        if len(digitos) == 10:
            b = False
        elif T* (j+1) == res:
            b = False
        else:
            j +=1
            res = T*j
    print "Case #" + str(i) +":",

    if len(digitos) == 10:
        print res
    else:
        print "INSOMNIA"
    i += 1
