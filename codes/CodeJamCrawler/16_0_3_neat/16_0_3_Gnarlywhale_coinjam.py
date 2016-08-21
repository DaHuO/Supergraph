__author__ = 'ThomasRiley'
from math import sqrt; from itertools import count, islice

primes = set()


def next_str(s):
    n = list(s)
    for c in range(len(n)-2, 0, -1):
        if n[c] == "0":
            n[c] = "1"
            return "".join(n)
        n[c] = "0"
    print("whoops")


def each_prime_base_check(s):
    facts = []
    for i in range(2, 11):
        if is_prime(int(s, i)):
            return True
        facts.append(prime_fac(int(s, i)))
    res = " ".join(map(str, facts))
    print("".join(s) +" "+ res)
    return False


def prime_fac(n):
    # Inspired by: http://stackoverflow.com/questions/171765/what-is-the-best-way-to-get-all-the-divisors-of-a-number
    d = 2
    while(d*d<=n):
        if n % d == 0:
            return d
        d += 1


def is_prime(n):
    # Shout out to stackoverflow: http://stackoverflow.com/questions/4114167/checking-if-a-number-is-a-prime-number-in-python
    if n not in primes and n > 1 and all(n % i for i in islice(count(2), int(sqrt(n)-1))):
        primes.add(n)
        return True
    return False


with open('input.txt') as f:
    testCases = f.readlines()
    n = int(testCases[0])
    for i in range(1, n+1):

        tc = testCases[i].split(" ")
        N = tc[0]
        J = int(tc[1])

        s = list("0"*int(N))
        s[0] = "1"
        s[-1] = "1"
        print("Case #1:")
        while J > 0:

            done = False

            while not done:

                if not each_prime_base_check("".join(s)):

                    done = True
                    s = next_str(s)
                else:

                    s = next_str(s)

            J -= 1
