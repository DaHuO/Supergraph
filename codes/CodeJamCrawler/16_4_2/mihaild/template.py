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


def get_p(a):
    K = len(a)
    probs = [0.0] * (K // 2 + 1)
    probs[0] = 1.0
    for c in a:
        next_probs = [0.0] * (K // 2 + 1)
        for i in range(len(probs)):
            if i > 0:
                next_probs[i] += probs[i - 1] * c
            next_probs[i] += probs[i] * (1.0 - c)
        probs = next_probs
    return probs[K // 2]


case_number = readint()
for case in range(case_number):
    N, K = readlinearray()
    p = readlinearray(float)
    p.sort()
    best = max(get_p(p[:K]), get_p(p[-K:]))
    ba = None
    for i in range(1, K // 2 + 1):
        a1 = p[:i] + p[-i:]
        add = K - len(a1)
        if add == 0:
            a = a1
            a.sort()
            best = max(best, get_p(a))
        else:
            for a2 in (p[i:][:add], p[:-i][-add:]):
                a = a1 + a2
                #print(a1, a2, i, K)
                assert(len(a) == K)
                a.sort()
                pr = get_p(a)
                if pr > best:
                    best = pr
    #for r in itertools.combinations(range(N), K):
        #r = list(r)
        #a = [p[i] for i in r]
        #if get_p(a) > best:
            #best = max(best, get_p(a))
            #ba = r
    #print(p, ba, best)
    print("Case #%d: %s" % (case + 1, best, ))
