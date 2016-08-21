#! /usr/bin/python3
import numpy, random
from math import sqrt; from itertools import count, islice

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def generateCoin(length, coins):
    genCoin = '1' + ''.join([str( random.randint(0,1) ) for k in range(length-2)]) + '1'

    while(genCoin in coins):
        genCoin = '1' + ''.join([str( random.randint(0,1) ) for k in range(length-2)]) + '1'

    return genCoin

T = int(input())

for i in range(T):
    N, J = map(int, input().split())
    coins = []

    print("Case #%i:" % (i+1), end = '')

    while len(coins) < J:
        tmpCoin = generateCoin(N, coins)
        validCoin = True

        for base in range(2, 11):
            if isPrime(int(tmpCoin, base)): 
                #print("%s is prime in base %i where it equals %i." % (tmpCoin, base, int(tmpCoin, base)))
                validCoin = False
                break
         
        if not validCoin: continue

        print("\n%s" % tmpCoin, end = ' ')
        coins.append(tmpCoin)

        for base in range(2, 11):
            decimalValue = int(tmpCoin, base)

            for potentialDivisor in range(2, int(sqrt(decimalValue))):
                if decimalValue % potentialDivisor == 0:
                    print(potentialDivisor, end = ' ')
                    break



