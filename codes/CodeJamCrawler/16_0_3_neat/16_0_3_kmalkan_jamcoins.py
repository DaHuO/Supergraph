import math

def printJamCoins(N,J):

    initCoin=firstCoin(N)
    jamCoin=initCoin
    printedCoins=0

    while printedCoins<J:
        primeDivisors,isJamCoin=checkJamCoin(jamCoin)
        if isJamCoin==True:
            printCoin(jamCoin,primeDivisors)
            printedCoins+=1
        jamCoin=getNextNum(jamCoin)

def printCoin(jamCoin,primeDivisors):
    primeStr=""
    for prime in primeDivisors:
        primeStr=primeStr+str(prime)+" "
    print jamCoin+" "+primeStr

def firstCoin(N):
    zeros=''
    for i in range(0,N-2):
        zeros=zeros+'0'
    zeros='1'+zeros+'1'
    return zeros

def getNextNum(jamCoin):
    jamCoin=jamCoin[:-1]
    nextCoin=bin(int(jamCoin,2)+1)[2:]
    return nextCoin+'1'


def checkJamCoin(jamCoin):
    primeDivisors=[]
    for i in range(2,11):
        numInOtherBase=binToBase(jamCoin,i)
        primeDiv=isPrime(numInOtherBase)
        if primeDiv==0:
            return (0,False)
        primeDivisors.append(primeDiv)
    return (primeDivisors,True)


def isPrime(numInOtherBase):
    for i in range(2,int(math.sqrt(numInOtherBase))+1):
        if numInOtherBase%i == 0:
            return i
    return 0


def binToBase(binNum,base):
    if binNum==0:
        return 0
    sum=0
    power=0
    for index in range(len(binNum)-1,-1,-1):
        sum+=int(binNum[index])*base**power
        power+=1
    return sum





num_cases=int(raw_input())
answers=[]
for i in range(0,num_cases):
    print "Case #"+str(i+1)+":"
    ip=raw_input().split(" ")
    N=int(ip[0])
    J=int(ip[1])
    printJamCoins(N,J)
# printResults(answers)

