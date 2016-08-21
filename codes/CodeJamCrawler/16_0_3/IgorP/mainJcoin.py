__author__ = 'igor'
import  itertools

from math import sqrt; from itertools import count, islice

usedDivisors=[]

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def findDivisor(n):
    for i in range(2, n-1):
        if n%i == 0:
            return i

def findCoinJ(n,j):
    counter = 1
    for item in itertools.product("10", repeat=n-2):
        num =''.join(['1']+list(item)+['1'])
        bases = []
        for i in range(2, 11):
            b = int(num, i)
            if isPrime(b):
                break
            else:
                bases.append(str(findDivisor(b)))
        else:
            print(' '.join([num]+bases))
            counter +=1
            if(counter >j):
                break





T = int(input())
for i in range(T):
    n,j = [int(x) for x in input().split()]
    print("Case #"+str(i+1)+":")
    findCoinJ(n,j)
