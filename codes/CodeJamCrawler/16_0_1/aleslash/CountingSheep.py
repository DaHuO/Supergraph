#!/usr/bin/python3
from sys import argv

script, filename = argv

txt = open(filename)

casos = int(txt.readline())

for caso in range(1,casos+1):
    N = int(txt.readline().strip())
    valores = '0123456789'
    vezes = 0
    if N != 0:
        
        while valores != '':
            vezes += 1
            obtido = N * vezes
            for numero in str(obtido):
                if numero in valores:
                    valores = valores.replace(numero,'')
        print("Case #%d: %s" %(caso,obtido))
    else:
        print("Case #%d: INSOMNIA" %(caso))
    
        
    
    