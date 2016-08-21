#!/usr/bin/env python

# Google Code Jam 2016
# Qualification Round
# C. Coin Jam
# patsp

import random

K_TIMEOUT_THRESHOLD = 10000

class TimeoutException(Exception):
    pass

def isPrime(x):
    k = 2
    while k * k <= x:
        if k > K_TIMEOUT_THRESHOLD:
            raise TimeoutException()
        if (x % k) == 0:
            return (False, k)
        k += 1
    return (True, None)

def test(maskBinStr):
    numbers = []
    divisors = []
    good = True
    for base in range(2, 11):
        x = int(maskBinStr, base)
        (prime, divisor) = isPrime(x)
        if prime:
            good = False
            break
        else:
            numbers.append(x)
            divisors.append(divisor)
    return (good, numbers, divisors)

nTests = int(input())
for t in range(1, nTests + 1):
    [n, j] = map(int, input().split())
    print('Case #{0}:'.format(t))
    cnt = 0
    #for mask in range(2**(n-1)-1, 2**n):
    numbersTaken = set()
    while True:
        mask = random.randint(2**(n-1)-1, 2**n)
        if not mask in numbersTaken:
            numbersTaken.add(mask)
            maskBinStr = '{0:b}'.format(mask)
            if len(maskBinStr) == n and maskBinStr[0] == '1' and maskBinStr[n - 1] == '1':
                try:
                    (good, numbers, divisors) = test(maskBinStr)
                    if good:
                        cnt += 1
                        print('{0} {1}'.format(maskBinStr, ' '.join(map(str, divisors))))
                        #print(' '.join(map(str, numbers)))
                    if cnt == j:
                        break
                except TimeoutException:
                    pass

