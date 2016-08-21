import os
import sys
import fileinput

def jamcoin_generator(n):
    """Returns all jamcoins of length n as base 10 ints"""
    for x in range(2**(n-2)):
        yield (
            (2 << (n-2))  # leading 1
            + (x << 1)    # middle digits
            + 1           # trailing 1
        )


for line in fileinput.input():
    if fileinput.lineno() == 1:
        continue

    N, J = [int(x) for x in line.split(' ')]
    break

i = 0

print "Case #1:"

for jamcoin in jamcoin_generator(N):
    divisors = []

    for base in range(2, 11):
        n = int(str(bin(jamcoin))[2:], base)

        for x in range(2, int(n**0.1) + 1):
            if (n % x == 0):
                divisors.append(x)
                break
        else:
            # The coin is prime
            break

    else:
        # Arrived at a valid jamcoin, so print output
        print bin(jamcoin)[2:], ' '.join(str(d) for d in divisors)
        i += 1

        if i >= J:
            break
