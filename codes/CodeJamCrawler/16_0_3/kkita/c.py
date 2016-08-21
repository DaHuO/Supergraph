#!/usr/bin/python
import itertools

T = int(input())
N = int(input())
J = int(input())

results = []
# iterate through all binary strings of length N
for b in itertools.product('01', repeat = N):
    if (b[0] != '1' or b[-1] != '1'): continue
    s = ''.join(b)
    divisors = []
    # bases 2-10
    for i in range(2,11):
        number = int(s,i)
        old_length = len(divisors)
        for j in range(2, int((number / 2))+1):
            if (number % j == 0):
                divisors.append(j)
                break
            if (j > 100000):
                break
        # number is prime, this is not a
        # jamcoin, skip to next number
        if len(divisors) == old_length:
            break
    if (len(divisors) == 9):
        results.append((s, divisors))
    if (len(results) == J): break

print("Case #1: ")
for (s, divs) in results:
    print("%s " % s, end="")
    for i in divs:
        print(i, end=" ")
    print('')
