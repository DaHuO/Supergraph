#!/usr/bin/env python

import math
import random


PRIME_LIMIT = 1000000
prime = []


def genPrime():
    isPrime = [True for i in range(PRIME_LIMIT)]
    
    for i in range(2, int(math.sqrt(PRIME_LIMIT) + 0.5)):
        if isPrime[i]:
            for j in range(i * 2, PRIME_LIMIT, i):
                isPrime[j] = False
    
    isPrime[0] = isPrime[1] = False
    for i in range(2, PRIME_LIMIT):
        if isPrime[i]:
            prime.append(i)
    
    
def read():
    return map(int, raw_input().split())


def work(cases, (N, J)):

    # (val, [base 2 divisor, base 3 divisor, ...])
    ans = []

    valSet = set([])
    
    while len(ans) < J:
        val = random.randrange(0, (1 << (N - 2)))
        val = (1 << (N - 1)) + (val << 1) + 1

        if val in valSet:
            continue
        
        divisor = []
        for base in range(2, 11):
            baseVal = 0
            for i in range(N):
                if val & (1 << i):
                    baseVal += base ** i
            
            for p in prime:
                if p * p > baseVal:
                    break
                if baseVal % p == 0:
                    divisor.append(p)
                    break

        if len(divisor) == 9:
            valSet.add(val)
            ans.append((format(val, 'b'), divisor))

    
    print "Case #%d:" % cases
    for (val, divisorList) in ans:
        print val, " ".join(map(str, divisorList))
    

if __name__ == "__main__":
    genPrime()
    
    for i in range(int(raw_input())):
        work(i + 1, read())
