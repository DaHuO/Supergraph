#!/usr/bin/env python3
import math
import random
import sys

#check if a number is prime in base10
def checkPrime(J):
    for i in range(2,math.floor(math.sqrt(J))):
       if (J % i) == 0:
           print(J,"is not a prime number")
           print(i,"times",J//i,"is",J)
           return i
    print(J,"is a prime number")
    return J

#check if a binary string interpret in base 2..10 is prime for all those base
#return a divisor for each base -1 if J is prime
def checkFullPrime(J):
    divisorSet=[]
    for i in range(2,11):
        Ji=int(J,i)
        p=checkPrime(Ji)
        if p==Ji:
            return -1
        else:
            divisorSet.append(str(p))
    return divisorSet


def main():
    inFile=open("dataset1.txt",'r')
    outFile=open("output1.txt",'w')
    print("Nombre de cas : "+str(int(inFile.readline())))
    dataset=inFile.readline().split(' ')
    numberSize=int(dataset[0])
    numberSize=numberSize-2
    caseNumber=int(dataset[1])
    random.seed()
    #a and b are the raznge in which the number is generate, there are choose to be sure the generate number respect the size ask in input.
    a=pow(2,numberSize-1)
    print(a)
    b=pow(2,numberSize)-1
    print(b)
    outFile.write("Case #1:\n");
    print("starting generating numbers")
    jamCoin=[]
    for i in range(0,caseNumber):
        divisorSet=-1
        while divisorSet==-1:
            N=random.randint(a,b)
            print(N)
            if N in jamCoin:#we don't want to accidentaly generate twice the same number
                continue
            J=bin(N)
            J='1'+J[2::]+'1'
            print(J)
            divisorSet=checkFullPrime(J)
            print(divisorSet)
        divisorString=" ".join(divisorSet)
        outFile.write(str(J)+" "+divisorString +"\n");
        jamCoin.append(J)
    inFile.close()
    outFile.close()
    return



main()