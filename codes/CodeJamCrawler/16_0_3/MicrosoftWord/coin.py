#!/usr/bin/python
import math

#f = open('in.txt')
def isprime(n):
    i = 0
    j = 0
    if n < 2:
        return False
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
def get_factor(n):
    i = 0
    j = 0
    if n < 2:
        return 2
    if n % 2 == 0 and n > 2:
        return 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return i


i = 0
n = 16
j = 50
total = 0
ts = []

for i in range(0, 2**(n-2)):
    num = 2**(n-1)
    num += 2*i
    num += 1
    s = bin(num)[2:]
    cur = 0
    good = 1
    for base in range(2, 11):
        number = 0
        for k in range(0, n):
            number += int(s[k])*(base**(n-k-1))
        if isprime(number):
            
            good = 0
            break
#        else:
#            print 's is ' + s + 'number is ' + str(number) + 'base' + str(base)

    if good == 1:
        ts.append(num)
        total += 1

    if total == j:
        break
print 'Case #1:'
        
if total == j:
    for i in range(0, total):
        s = bin(ts[i])[2:]
        string = s + ' '
        for base in range(2, 11):
            number = 0
            for k in range(0, n):
                number += int(s[k])*(base**(n-k-1))
            fac = get_factor(number)
            if base != 10:
                string = string + str(fac) + ' '
            else:
                string = string + str(fac)
        print string
