#!/bin/python

from math import sqrt, ceil

global primes
primes = []

def getNumInBase(num, base):
    if base == 10:
        return num

    transnum = 0
    d = 0
    while( num > 0 ):
        transnum += (num % 10) * base**d;
        d+=1
        num = int(num/10)

    return transnum

def printIfJamCoin(coin):
    divisors = [0] * 9;

    for base in range(2, 11):
        translation = getNumInBase(coin, base)
        divisor = getDivisor(translation)

        #print("{0} : {1} / {2}".format(base, translation, divisor))
        if divisor == 1:
            return False
        else:
            divisors[base-2] = divisor

    print("{0} {1}".format(coin, " ".join(str(i) for i in divisors)))
    return True

def getDivisor(num):
    s = int(sqrt(num));
    i = 0
    nprimes = len(primes)
    while( i < nprimes and primes[i] <= s ):
        if num % primes[i] == 0:
            return primes[i]
        i+=1

    """
    if(i == nprimes and primes[i-1] < s):
        for k in range(primes[i-1], s+1, 2):
            if num % k == 0:
                return k
    """

    return 1

def isPrime(num):
    s = int(sqrt(num));
    i = 1
    while primes[i] <= s:
        if num % primes[i] == 0:
            return False;
        i+=1;
    return True;

def calcPrimesUpTo(limit):
    global primes
    primes += [2,3,5]
    for num in range(7, limit+1, 2):
        if( isPrime(num) ):
            primes += [num]

def getLimit(N):
    limit = 1
    for i in range(N):
        limit *= 10
        limit += 1
    return limit

def getFirstCoin(N):
    return 10 ** (N-1) + 1

if __name__ == '__main__':

    TT = int(input())
    N,L = [int(i) for i in input().split(" ")]

    calcPrimesUpTo( 1000000 )

    print("Case #1:")

    total = 0
    limit = getLimit(N)
    count = 0
    coin = getFirstCoin(N)
    from time import time
    startTime = time()
    prevTime = time()
    while count < L and coin <= limit:

        if( printIfJamCoin(coin) ):
            count += 1
        coin = eval(bin( eval( '0b' + str(coin) ) + 2 )[2:])

        """
        total += 1
        if( total % 100 == 0 ):
            print( "{0:.2f} {1:.2f}".format( time() - startTime, time() - prevTime ) )
            prevTime = time()
        """




