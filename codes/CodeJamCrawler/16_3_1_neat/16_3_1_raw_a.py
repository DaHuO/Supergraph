#!/usr/bin/python3

from operator import methodcaller, is_not
from itertools import repeat, zip_longest, chain, groupby

def filterNone(iterable):
    return filter(lambda x: x is not None, iterable)

def chunked(n, iterable):
    args = [iter(iterable)] * n
    return map(filterNone, zip_longest(*args))

for i in range(1, 1 + int(input())):
    print('Case #{}: '.format(i), end='')
    party_count = int(input())
    parties = (repeat(chr(ord('A') + i), int(p)) for i, p in enumerate(input().split()))
    plan = []
    for _, g in groupby(zip_longest(*parties), key=methodcaller('count', None)):
        plan.extend(map(''.join, chunked(2, chain.from_iterable(filterNone(g)))))
    plan.reverse()
    print(' '.join(filter(bool, plan)))
