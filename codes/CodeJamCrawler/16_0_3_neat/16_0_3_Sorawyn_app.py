import math
import sys

N = 32
J = 500
# N = 6
# J = 3

smallest = 2 ** (N - 2)
biggest = 2 ** (N - 1)


def to_str(num):
    return str(bin(num))[2:] + '1'

#primes = [True] * 100000001
primes = [True] * 1000001
for i in xrange(2, int(math.ceil(math.sqrt(len(primes))))):
    if primes[i]:
        for k in xrange(i + i, len(primes), i):
            primes[k] = False

primes = [x[0] for x in enumerate(primes) if x[1] is True][2:]

print "Case #1:"
counts = 0
for template in xrange(smallest, biggest):
    str_num = to_str(template)
    assert len(str_num) == N
    divisors = []
    bad = False
    for base in range(2, 11):
        if bad:
            break
        val = int(str_num, base)
        for p in primes:
            if p * p > val or p == val:
                bad = True
                break
            if val % p == 0:
                divisors.append(p)
                break
            bad = True
            break

    if len(divisors) == 9:
        print str_num,
        for d in divisors:
            print d,
        print

        counts += 1
        if counts == J:
            break
