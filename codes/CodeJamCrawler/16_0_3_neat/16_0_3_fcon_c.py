#!/usr/bin/python

from math import ceil, sqrt
import sys


max_prime = 65536



def sieve(n):
    result = []
    work = n*[True]
    limit = int(ceil(sqrt(n)))
    
    result += [2]
    
    i = 3;
    
    while i < limit:
        if work[i]:
            result += [i]
            
            for j in xrange(2*i, n, i):
                work[j] = False
        
        i += 2
    
    while i < n:
        if work[i]:
            result += [i]
        i += 2
    
    return set(result)


def find_divisor(n, primes):
    limit = int(ceil(sqrt(n)))
    
    if n < max_prime and n in primes:
        return 0
    
    for p in primes:
        if p >= limit:
            break
        
        if n % p == 0:
            return p
    
    return 0


def next_number(num):
    i = N - 2
    
    while num[i] == 1:
        num[i] = 0
        i -= 1
    
    num[i] = 1
    
    return num


def to_base(num, b):
    result = 0
    
    for i in xrange(N):
        if num[N-i-1]:
            result += b ** i
    
    return result


primes = sieve(max_prime)


N = 16
J = 50

f = open('output_small.txt', 'w')

f.write('Case #1:\n')

num = [1] + [0]*(N-2) + [1]
j = 0

while j < J:
    to_print = []
    
    b = 2
    tmp = 0
    
    while b < 11:
        tmp = to_base(num, b)
        divisor = find_divisor(tmp, primes)
        
        if divisor == 0:
            break
        
        to_print += [divisor]
        b += 1
    
    if b == 11:
        j += 1
        f.write('%d' % tmp)
        
        for i in to_print:
            f.write(' %d' % i)
        
        f.write('\n')
    
    num = next_number(num)

f.close()



N = 32
J = 500

f = open('output_large.txt', 'w')

f.write('Case #1:\n')

num = [1] + [0]*(N-2) + [1]
j = 0

while j < J:
    to_print = []
    
    b = 2
    tmp = 0
    
    while b < 11:
        tmp = to_base(num, b)
        divisor = find_divisor(tmp, primes)
        
        if divisor == 0:
            break
        
        to_print += [divisor]
        b += 1
    
    if b == 11:
        j += 1
        f.write('%d' % tmp)
        
        for i in to_print:
            f.write(' %d' % i)
        
        f.write('\n')
    
    num = next_number(num)

f.close()

