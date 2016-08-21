__author__ = 'pavlovick'
import random
import numpy as np
import math
class Primes:
    def __init__(self, n):
        self.n=n+1
        self.integersVec=np.ones(self.n,dtype=np.int)
        self.primeVector=np.array([2]) #Setup primes vector. First elment is 2


    def integersVectorSetup(self): #Setup ones vector of the dimention of n. 1 and 2 multiples are setted to zero.
        self.integersVec[1]=0
        self.integersVec[[i for i in range(0,self.n,2)]]=0
        return self.integersVec

    def eratosteneIteration(self,k):
        pos=[i for i in range(k,self.n,k) ]
        self.integersVec[pos]=0
        return self.integersVec

    def lastPrime(self):
        return self.primeVector[-1]

    def nextPrime(self):
        return next((idx for idx in range(self.lastPrime(),self.n) if self.integersVec[idx]), None)

    def Eratostene(self):
        self.integersVectorSetup()
        while(self.nextPrime()<math.sqrt(self.n)):
            nextPrime=self.nextPrime()
            self.eratosteneIteration(nextPrime)
            self.primeVector=np.append(self.primeVector,nextPrime)
        self.primeVector=np.append(self.primeVector,np.nonzero(self.integersVec))
        return self.integersVec


SET_BIN = set('01')
def isPrime2(n, primeVec):
    if n==2 or n==3: return True , n
    if n%2==0 or n<2: return False, 2
    for i in primeVec:
        if n%i==0 and n>i:
            print i
            return False, i
    return True, i

def stringAsBase(stringNumber, base):
    baseNumber=0
    position = len(stringNumber)-1
    for digit in stringNumber:
        baseNumber= baseNumber+ int(digit) * (base**position)
        position = position -1
    return baseNumber

def randomBase10(length):
    stringNumber='1'
    possibleChars = ['0', '1']
    while len(stringNumber)< length-1:
        stringNumber= stringNumber + str(random.sample(SET_BIN, 1)[0],)
    stringNumber = stringNumber +'1'
    return stringNumber

def randomBase10NonPrime(lenght):
    isNotPrime = False
    randomNumber =0
    while isNotPrime == False:
        randomNumber = randomBase10(lenght)
        if randomNumber.count('1')%3==0:
            isNotPrime = True
    return randomNumber
def isNotPrimeInOtherBases(number, dictionaryProof, primeVec):
    for base in range(9, 1, -1):
        baseJamCoin = stringAsBase(number, base)
        primeTest= isPrime2(baseJamCoin, primeVec)
        if primeTest[0] == True:
            return False, dictionaryProof
        dictionaryProof[base]= primeTest[1]
    return True, dictionaryProof


def selectJamCoin(lenght, primeVec):
    isJamCoin=False
    possibleJamCoin =0
    while isJamCoin==False:
        dictionaryProof={}
        possibleJamCoin = randomBase10NonPrime(lenght)
        dictionaryProof[10]= 3
        possibleJamCoinTest=isNotPrimeInOtherBases(possibleJamCoin, dictionaryProof, primeVec)
        if possibleJamCoinTest[0]:
            isJamCoin = True
    return possibleJamCoin, possibleJamCoinTest[1]



p=Primes(100000)
p.Eratostene()
primeVec= p.primeVector
N_MAX=500
N_DIM=32
jamCoinList=[]
solution = open('solution.txt', 'w')
solution.write('Case #1:\n')
for i in range(0, N_MAX):
    print i
    jamCoin, jamCoinDict= selectJamCoin(N_DIM, primeVec)
    if jamCoin in jamCoinList:
        i= i-1
    else:
        newLine= str(jamCoin)
        for base in range(2,11):
            newLine = newLine+' '+ str(jamCoinDict[base])
        print newLine
        solution.write(newLine + '\n')



