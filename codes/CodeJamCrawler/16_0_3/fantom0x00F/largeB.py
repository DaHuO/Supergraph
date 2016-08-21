import socket
import hashlib
import datetime
import time
from time import sleep

def addzero(stroke):
    if (len(stroke) >=30):
        print("PLEASE STOP!!!!")
    while len(stroke) != 30:
        stroke = "0"+stroke
    return stroke

def countOne(stroke):
    count = 0
    for i in range(0,len(stroke)):
        if (stroke[i] == '1'):
            count+=1
    return count

def checkDivBy11(stroke,base):
    firstSumm = 0
    secondSumm = 0
    for i in range(0,len(stroke)):
        if stroke[i] == '1':
            if (i%2 == 0):
                firstSumm+=1
            else:
                secondSumm+=1
    if (abs(firstSumm-secondSumm) % (base+1) == 0):
        return True
    return False

def isPrime(n):
    if (n%2==0):
        return 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    if d*d > n:
        return -1
    return d

f = open('largeB.out','w')
f.write('Case #1:\n')

middle = 0
count = 0

while count!=500:
    if (countOne(addzero(bin(middle)[2:]))%2==0):
        tested = "1"+addzero(bin(middle)[2:])+"1"
        ans = []
        used = True
        for i in range(2,11):
            if (i%2==0):
                if (checkDivBy11(tested,i)):
                    d = i+1
                else:
                    d = -1
            else:
                d = 2
            if d==-1:
                used = False
                break
            ans.append(d)
        if used:
            count+=1
            print(tested+" ",end="")
            f.write(tested+" ")
            for k in ans:
                print(str(k)+" ",end="")
                f.write(str(k)+" ")
            print("")
            f.write("\n")
    middle+=1

f.close()
