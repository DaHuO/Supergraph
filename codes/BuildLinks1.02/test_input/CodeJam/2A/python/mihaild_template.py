import string
import itertools

def readint():
    return int(input())


def readfloat():
    return float(input())


def readarray(N, foo=input):
    return [foo() for i in range(N)]


def readlinearray(foo=int):
    return list(map(foo, input().split()))


def GCD(a, b):
    while b:
        a, b = b, a % b
    return a


def gen_primes(max):
    primes = [1]*(max+1)
    for i in range(2, max+1):
        if primes[i]:
            for j in range(i+i, max+1, i):
                primes[j] = 0
    primes[0] = 0
    return [x for x in range(2, max+1) if primes[x]]


case_number = readint()
for case in range(case_number):
    n, r, p, s = readlinearray()
    c = list('p' * p + 'r' * r + 's' * s)
    ok = False
    solutions = []
    for perm in itertools.permutations(c):
        prev = perm
        while True:
            #print(prev)
            n = False
            if len(prev) == 1:
                ok = True
                okperm = perm[:]
                break
            x = []
            for i in range(1, len(prev), 2):
                if prev[i - 1] == 'p' and prev[i] == 'r' or prev[i - 1] == 'r' and prev[i] == 'p':
                    x.append('p')
                elif prev[i - 1] == 'r' and prev[i] == 's' or prev[i - 1] == 's' and prev[i] == 'r':
                    x.append('r')
                elif prev[i - 1] == 's' and prev[i] == 'p' or prev[i - 1] == 'p' and prev[i] == 's':
                    x.append('s')
                else:
                    n = True
            if n:
                break
            if len(prev) % 2:
                x.append(prev[-1])
            if x == prev:
                break
            prev = x
        if ok:
            solutions.append(''.join(perm))
        ok = False
    if solutions:
        print("Case #%d: %s" % (case + 1, min(solutions).upper(), ))
    else:
        print("Case #%d: IMPOSSIBLE" % (case + 1, ))
