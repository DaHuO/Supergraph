#!/usr/bin/env python
#raw input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
digitos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
def listarNum(x): 
    return list(map(int, str(x)))

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n = int(raw_input())  #lee una entrada y convierte en entero
    for k in range(1,501):
        lista = listarNum(k * n)  #separa la entrada en una lista de enteros digitos
        for j in lista:
            if j in digitos:
                digitos.remove(j)
                if digitos == []:
                    break
        if digitos == []:
            print "Case #{}: {}".format(i, k*n)
            break
    if digitos != []:
        print "Case #{}: INSOMNIA".format(i)  
    digitos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  

    
    # check out .format's specification for more formatting options
