from __future__ import print_function
import math

entrada = open("in.txt", "r+")
salida = open("out.txt", "r+")


palabras={'Z':[0],'G':[8],'X':[6],'W':[2],'U':[4],
          'S':[6,7],'H':[8,3],'F':[4,5],'I':[6,5],'V':[5,7],
          'R':[0,3,4],'N':[1,9,7],'T':[2,3,8],
          'O':[0,1,2,4] ,'E':[0,1,3,5,7,8,9]
            }
solucion=[]
cases = int(entrada.readline())

def replace0(cadena):
    solucion.append(0)
    cadena.remove('Z')
    cadena.remove('E')
    cadena.remove('R')
    cadena.remove('O')
def replace1(cadena):
    solucion.append(1)
    cadena.remove('E')
    cadena.remove('N')
    cadena.remove('O')
def replace2(cadena):
    solucion.append(2)
    cadena.remove('O')
    cadena.remove('W')
    cadena.remove('T')
def replace3(cadena):
    solucion.append(3)
    cadena.remove('E')
    cadena.remove('E')
    cadena.remove('R')
    cadena.remove('H')
    cadena.remove('T')
def replace4(cadena):
    solucion.append(4)
    cadena.remove('R')
    cadena.remove('U')
    cadena.remove('O')
    cadena.remove('F')
def replace5(cadena):
    solucion.append(5)
    cadena.remove('E')
    cadena.remove('V')
    cadena.remove('I')
    cadena.remove('F')
def replace6(cadena):
    solucion.append(6)
    cadena.remove('X')
    cadena.remove('I')
    cadena.remove('S')
def replace7(cadena):
    solucion.append(7)
    cadena.remove('N')
    cadena.remove('E')
    cadena.remove('V')
    cadena.remove('E')
    cadena.remove('S')
def replace8(cadena):
    solucion.append(8)
    cadena.remove('T')
    cadena.remove('H')
    cadena.remove('G')
    cadena.remove('I')
    cadena.remove('E')
def replace9(cadena):
    solucion.append(9)
    cadena.remove('N')
    cadena.remove('I')
    cadena.remove('N')
    cadena.remove('E')

contador=0

for i in range(1, cases+1):
    cadena =list(entrada.readline()[:-1])
    while('Z' in cadena or 'G' in cadena or 'X' in cadena  or 'U' in cadena or 'W' in cadena  and contador<10):
        #print("condicion 1")
        contador= contador+1
        if 'Z' in cadena:
            replace0(cadena)
        if 'G' in cadena:
            replace8(cadena)
            if 'T' in cadena and 'H' in cadena and 'R'  in cadena and cadena.count('E')>=2 :
                replace3(cadena)
                if 'T'  in cadena and 'W'  in cadena and 'O' in cadena:
                    replace2(cadena)
        if 'X' in cadena:
            replace6(cadena)
            if 'S' in cadena and 'E' in cadena and 'V' in cadena and 'E' in cadena and 'N' in cadena:
                replace7(cadena)
            if 'F' in cadena and 'I' in cadena and 'V' in cadena and 'E' in cadena:
                replace5(cadena)
        if 'U' in cadena:
            replace4(cadena)
            if 'F' in cadena and 'I' in cadena and 'V' in cadena and 'E' in cadena:
                replace5(cadena)
        if 'W' in cadena:
            replace2(cadena)
    contador =0
    while(contador<10 and ('S' in cadena or 'H' in cadena or 'F' in cadena  or 'I' in cadena or 'V' in cadena ) ):
        #print("condicion 2")
        contador= contador+1
        if 'S' in cadena and 'E' in cadena and 'V' in cadena and 'E' in cadena and 'N' in cadena:
            replace7(cadena)
        if 'T' in cadena and 'H' in cadena and 'R' in cadena and cadena.count('E')>=2:
            replace3(cadena)
        if 'F' in cadena and 'I' in cadena and 'V' in cadena and 'E' in cadena  :
            replace5(cadena)
    contador =0
    while('R' in cadena or 'N' in cadena or 'T'  in cadena and contador<10):
        #print("condicion 3")
        contador= contador+1
        if 'N' in cadena and 'I' in cadena and 'N' in cadena and 'E' in cadena  :
            replace9(cadena)
        if 'O' in cadena and 'N' in cadena and 'E':
            replace1(cadena)
    contador =0

    #print(cadena)
    if(cadena==[]):
        solucion.sort()
        salida.write("Case #"+str(i)+": ")
        for sol in solucion:
            #print(sol, end="")
            salida.write(str(sol))
        salida.write("\n")
        #print()
    solucion=[]
