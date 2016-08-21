#!/usr/bin/env python3

def gen_primes(to):
    primes = [2]
    for n in range(3, to+1, 2):
        prime = True
        j = 2
        while j*j <= n:
            if n % j == 0:
                prime = False
                break
            j += 1
        if prime:
            primes.append(n)
    return primes

def test(num):
    for prime in primes:
        if prime*prime > num:
            break
        if num % prime == 0:
            return prime
    return 0

T = int(input())

primes = gen_primes(65536)

for t in range(0, T):
    N, J = [int(x) for x in input().split()]

    mask = (1 << (N-1)) | 1
    limit = 2**(N-2)

    print("Case #{0}:".format(t+1))
    found = 0

    for i in range(0, limit):
        factors = []
        num = str(bin(mask | (i << 1)))[2:]

        for base in range(2, 11):
            conv = int(num, base)
            div = test(conv)
            if div != 0:
                factors.append(div)
            else:
                break

        if len(factors) == 9:
            s = num
            for factor in factors:
                s += " " + str(factor)
            print(s)
            found += 1

        if found == J:
            break
                
