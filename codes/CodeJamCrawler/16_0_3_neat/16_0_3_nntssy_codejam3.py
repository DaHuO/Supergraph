# -*- coding: utf-8 -*-
def strToNumBase(numStr,base):
    if numStr=='1':
        return 1
    elif base==10:
        return int(numStr)
    else:
        power=len(numStr)-1
        num=0
        for digit in numStr:
            if digit=='1':
                num+=base**power
            power-=1
        return num

def getPrimes(num):
    primes=[]
    for i in xrange(2,num+1):
        j=0
        isPrime=True
        while j<len(primes) and isPrime:
            if i%primes[j]==0:
                isPrime=False
            j+=1
        if isPrime:
            primes.append(i)
    return primes
    
def getDivisorLimited(num,limit):
    i=0
    result=True
    if int(num**(0.5))<limit:
        primes=getPrimes(int(num**(0.5)))
        limit=False
    else:
        primes=getPrimes(limit)
        limit=True
    numPrimes=len(primes)
    while result and i<numPrimes:
        if num%primes[i]==0:
            result=False
            limit=False
        i+=1
    if limit:
        return -2
    elif result or primes==[]:
        return -1
    else:        
        return primes[i-1]    
                                
def produceJamCoins(numCoins,length):
    if length<=3:
        return None
    else:
        jamCoins={}
        num=0
        maxNum=2**(length-2)
        while len(jamCoins)!=numCoins and num<maxNum:
            binNum=bin(num)[2:]
            binNumLen=len(binNum)
            if binNumLen!=length-2:
                binNum=(length-2-binNumLen)*'0'+binNum
            coin='1'+binNum+'1'
            coinDivisors=[]
            result=True
            base=2
            while result and base<=10:
                coinToBase=strToNumBase(coin,base)
                divisor=getDivisorLimited(coinToBase,10**3)
                if divisor==-1 or divisor==-2:
                    result=False    
                else:
                    coinDivisors.append(divisor)
                base+=1 
            if base==11 and len(coinDivisors)==9:
                jamCoins[coin]=coinDivisors   
            num+=1                   
        return jamCoins    
     
def main(fout):
    fout.write('Case #'+str(1)+': \n')
    jamCoins=produceJamCoins(500,32)
    for coin in jamCoins.keys():
        fout.write(coin)
        for divisor in jamCoins[coin]:
            fout.write(' '+str(divisor))
        fout.write('\n')    
        
fout=open('C:\Users\exin1\Google Drive\Study\Google CodeJam\C.out','w')
main(fout)
fout.close()     