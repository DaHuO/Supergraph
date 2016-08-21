#!/usr/bin/python3
from random import randint

t = int(input())

for test in range(1, t+1):
    K, C, S = map(int, input().split())
    v = list(range(1, 1+S))

    """
    n = K**C
    for i in range(S-2):
        x = randint(1, n)
        while x in v:
            x = randint(1, n)
        v.append(x)

    v = list(set(v))
    """
    print("Case #%i: " % test, end='')
    print("%s" % ' '.join([str(x) for x in v]))
