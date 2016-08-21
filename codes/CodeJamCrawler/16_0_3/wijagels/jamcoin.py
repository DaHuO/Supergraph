import numpy as np
import math

globprimes = []


def main():
    for i in range(1, int(input()) + 1):
        print('Case', '#' + str(i) + ':')
        done = 0
        inp = input().split()
        length = int(inp[0])
        start = int(pow(2, length - 1))
        cur = start
        for cur in range(start, start * 2):
            divisors = [0] * 9
            if cur % 2 is 0:
                continue
            for i in range(2, 11):
                b = int(np.base_repr(cur, 2), i)
                # print(np.base_repr(cur, 2), i, b)
                divisors[i-2] = factor(b)
            if 0 in divisors:
                # print(divisors)
                continue
            else:
                done += 1
                divisors = [str(k) for k in divisors]
                print(format(cur, 'b'), ' '.join(divisors))
                if done >= int(inp[1]):
                    break


def primepop(m):
    for i in range(2, int(math.sqrt(float(m)))):
        if isprime(i):
            globprimes.append(i)


def isprime(i):
    return factor(i) is 0


def factor(i):
    for d in globprimes:
        if d > math.sqrt(float(i)):
            return 0
        if i % d is 0:
            return d
    return 0


primepop(2**16) # We don't need that many primes, since we just care about factors
main()
