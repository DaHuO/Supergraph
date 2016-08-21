#!/usr/bin/python3

def prime_list(approx):
    #"Borrowed" http://stackoverflow.com/questions/3939660/sieve-of-eratosthenes-finding-primes-python
    limit = approx * 10
    sieve = [True] * limit
    sieve[0] = sieve[1] = False

    for(i, isprime) in enumerate(sieve):
        if isprime:
            yield i
            for n in range(i*i, limit, i):
                sieve[n] = False

def first_divisor(number, prime_list):
    for prime in prime_list:
        if number % prime == 0:
            return prime
    return None

import random

def codejammer():
    rounds = int(input())
    bits, howmany = [int(x) for x in input().split()]
    print("Case #{}: {}".format(1, ""))

    some_primes = list(prime_list(500))
    seed = 2**(bits-1)+1  # odd

    for i in range(howmany):
        while True:
            seed += 2*random.randint(1, 8) # even
            s = bin(seed)[2:]
            divs = [first_divisor(int(s, base), some_primes)
                    for base in range(2, 11)]
            divs = [d for d in divs if d]
            if len(divs) >= 9:
                break
        print(bin(seed)[2:], " ".join([str(d) for d in divs]))
    return


if __name__ == '__main__':
    codejammer()

