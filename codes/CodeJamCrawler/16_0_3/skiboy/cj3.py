#!/usr/bin/python -u
import itertools
from math import sqrt

# Part of 2016 Google code jam

# This task validates jamcoins (a number of 1's or 0's which only has primes for base 2-10)
def find_jamcoins(n, j):
    n = n -2

    # loop through numbers until the required number of jamcoins are found
    for a in range((n)**2): 
        block = str(bin(a))[2:]
        d = (n)-len(block)

        if d != 0:
            block = '0' * d + block

        jamcoin = '1' + block + '1'
        non_primes=[]
        divisors=[]

        # determine base values
        l = list(jamcoin)

        for base in range(2,11):
            value=0
            power=0
            for i in range(len(l)-1,-1,-1):
                if l[i] == '1':
                    value = value + base**power
                power = power + 1
    
            divisor = return_divisor(value)
            if divisor == 0:
                break
            else:
                non_primes.append(value)
                divisors.append(str(divisor))

        if len(non_primes) == 9:
            print jamcoin + ' ' + ' '.join(divisors)
            #print '   primes ' + str(non_primes)
            #print '   divisors ' + str(divisors)
            j = j - 1

            if j == 0:
                break

# checking for primes is a classic problem, I pulled this optimized version off the web
def return_divisor(n):
    if n == 2 or n == 3: 
        return 0
    elif n < 2 or n % 2 == 0: 
        return n/2
    elif n < 9:
        return 0
    elif n % 3 == 0: 
        return n/3
    r = int(sqrt(n))
    f = 5
    while f <= r:
        if n % f == 0 :
            return n/f
        elif n % (f + 2) == 0: 
            return n / (f + 2)
        else:
            f += 6
    return 0


T = int(raw_input().strip())

for i in range(1, T+1):
    n,j = map(int, raw_input().split())
    print 'Case #' + str(i) + ':'
    find_jamcoins(n,j)
