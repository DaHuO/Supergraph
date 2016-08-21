#!/bin/python
from math import sqrt; from itertools import count, islice
from sympy.ntheory import primefactors, isprime, divisor_count


f = open('test.txt', 'r')
output = open('output.txt', 'w')

output.write('Case #1:\n')

f.readline()
inp = f.readline()
length = int(inp.split()[0])
amount = int(inp.split()[1])

counter = 0
cur_num = 1
while counter < amount:
    enclosed_num = "{0:b}".format(cur_num)
    while len(enclosed_num) != length -2:
        enclosed_num = "0" + enclosed_num

    enclosed_num = "1" + enclosed_num + "1"

    check = True
    bases = []
    for i in range(2, 11):
        base = int(enclosed_num, i)
        bases.append(base)
        if isprime(base):
            check = False
            break

    #print(len(bases))
    if check == True:
        print(enclosed_num, end="")
        output.write(enclosed_num)
        for base in bases:
            if divisor_count(base) == 2:
                print("dafuq")
            print(' ', end="")
            print(primefactors(base)[0], end="")
            output.write(" ")
            output.write(str(primefactors(base)[0]))
        print()

        for base in bases:
            print('{} -> {}'.format(base, primefactors(base)))
        output.write("\n")
        counter += 1
        
    #if cur_num % 10 == 0:
    #    print(cur_num)
    cur_num += 1
    if cur_num > 2**(length-2):
        break

f.close()
output.close()

