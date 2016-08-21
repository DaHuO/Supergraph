from math import *
from itertools import *
def someDiv(n):
    i = 2
    while i < ceil(sqrt(n)):
        if n%i == 0:
            return i
        i = i + 1
    return -1

def isJamCoin(a):
    lista = [a]
    b2 = someDiv(int(a, 2))
    if b2 != -1:
        lista.append(b2)
    b3 = someDiv(int(a, 3))
    if b3 != -1:
        lista.append(b3)
    b4 = someDiv(int(a, 4))
    if b4 != -1:
        lista.append(b4)
    b5 = someDiv(int(a, 5))
    if b5 != -1:
        lista.append(b5)
    b6 = someDiv(int(a, 6))
    if b6 != -1:
        lista.append(b6)
    b7 = someDiv(int(a, 7))
    if b7 != -1:
        lista.append(b7)
    b8 = someDiv(int(a, 8))
    if b8 != -1:
        lista.append(b8)
    b9 = someDiv(int(a, 9))
    if b9 != -1:
        lista.append(b9)
    b10 = someDiv(int(a, 10))
    if b10 != -1:
        lista.append(b10) 
    return lista

tests = int(raw_input())
for q in range(tests):
    size,qnt = map(int, raw_input().split())
    v = int(pow(10,size-1) + 1)
    j = 0
    meio = map(''.join, product('01', repeat=size-2))
    meio_index = 0
    while(j < qnt):
        coin = "1"
        coin = coin + meio[meio_index] + "1"
        print("Case #%d:") % (j+1)
        if(len(isJamCoin(coin)) == 10):
            for r in isJamCoin(coin):
                print(r),
            print("")
            j = j + 1
        meio_index = meio_index + 1





