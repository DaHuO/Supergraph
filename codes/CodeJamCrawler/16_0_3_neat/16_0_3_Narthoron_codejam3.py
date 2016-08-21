from math import sqrt; from itertools import count, islice
from time import time
import itertools

def isPrime(n):
    if n < 2: return False
    for number in islice(count(2), int(sqrt(n)-1)):
        if not n%number:
            return False
        if(time()-t > 1):
            return True
    return True

def checkPrime(n):
    for r in range(2,11):
        if isPrime(int(n,r)):
            return  False
    return True

def prime_power(n):
    # c goes through 2, 3, 5, then the infinite (6n+1, 6n+5) series
    for c in itertools.accumulate(itertools.chain([2, 1, 2], itertools.cycle([2,4]))):
        if c*c > n: break
        if n%c: continue
        d,p = (), c
        while not n%c:
            n,p,d = n//c, p*c, d + (p,)
        return(d[0])
    if n > 1: return((n))

def findDivs(n):
    for r in range(2,11):
        num = int(n,r)
        # for d in range(2, num):
        #     if num % d == 0:
        #         break
        print(' ',prime_power(num), end='', sep='')


x = input()
t = time()
for i in range(int(x)):
    inputs = input().split()
    Je = int(inputs[0])
    Ne = int(inputs[1])
    iter = 0
    print("Case #",i+1,":", sep='')
    for string in map(''.join, itertools.product('01', repeat=Je-2)):
        jamcoin = '1'+string+'1'
        t = time()
        if checkPrime(jamcoin):
            print(jamcoin, end='', sep='')
            findDivs(jamcoin)
            print()
            iter += 1
            if iter == Ne:
                break
