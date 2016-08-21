#!/usr/bin/env python

import sys
import math

# Cases
f = open(sys.argv[1])
cases = f.readlines()
len_cases = int(cases[0])

# Is the number prime?
# def is_prime(a):
#     return a > 1 and all(a % i for i in xrange(2, a))
def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))
# def is_prime(n):
#     return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

# Every possible base is prime?
def getBase(num):
    for i in range(2,11):
        if is_prime(int(num, i)):
            return False
    return True

# What is the smallest non-trivial divisor?
def smallestnontrivial(n):
    d = 2
    while n % d != 0:
        d = d+1
    return d

# Processing each case
for i in range(1, len_cases+1):
    N,J = cases[i].split(' ')
    results = []
    middl = '0' * (int(N) - 2)
    while len(results) < int(J) and len(middl) < int(N) - 1:
        if getBase('1' + middl + '1'):
            results.append('1' + middl + '1')
            middl = '{:0{}b}'.format(long(middl, 2) + 1, len(middl))
        else:
            middl = '{:0{}b}'.format(long(middl, 2) + 1, len(middl))
    print "Case #%d:" % (i)
    for result in results:
        print result, smallestnontrivial(int(result, 2)), smallestnontrivial(int(result, 3)), smallestnontrivial(int(result, 4)), smallestnontrivial(int(result, 5)), smallestnontrivial(int(result, 6)), smallestnontrivial(int(result, 7)), smallestnontrivial(int(result, 8)), smallestnontrivial(int(result, 9)), smallestnontrivial(int(result, 10))
