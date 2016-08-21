# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 17:22:00 2016

@author: madushan
"""
import itertools
import random

N = 32
J = 500
result = []
hN = N/2

def modulo(a, b, c):
    x = 0
    y = a % c
    while b > 0:
        if b % 2 == 1:
            x = (x + y) % c
        y = (y * 2) % c
        b /= 2
    return x % c

def compositeTest(num, iterations):
    if num == 1:
        return False
    for i in xrange(iterations):
        a = random.randrange(1, num - 1)
        if(modulo(a, num - 1, num)):
            return True
    return False

def testforDevisors(num):
    for i in xrange(2, int(num ** 0.5)):
        if num % i == 0:
            return i

print 'Case #1:'
for item in itertools.product([0,1], repeat = hN - 1):
    fS = '1' + '{}' * (hN - 1)
    numS = fS.format(*item) + fS.format(*item)[::-1]
    devisors = []
    for base in xrange(2, 11):
        num = int(numS, base)
        if base % 2 == 1:
            composteF = compositeTest(num, 10)
            if composteF == False:
                break
        devisors.append(testforDevisors(num))
    result.append([numS, devisors])
    if composteF == False:
        continue
    if len(result) == J:
        break

for item in result:
    print item[0],
    for devisor in item[1]:
        print devisor,
    print ''