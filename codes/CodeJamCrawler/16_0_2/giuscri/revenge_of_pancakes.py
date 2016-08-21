from functools import reduce
import math

import time

def all_happy_faces(s):
    return '-' not in s

def flip_first(s, k):
    lst = list(s)
    for i in range(0, k):
        lst[i] = '-' if lst[i] == '+' else '+'
    return ''.join(lst)

def shrink(s):
    ret = s[0]
    for c in s:
        if c != ret[-1]:
            ret += c
    return ret

'''
def fn(s, c, costs, ancestors, blacklist, cache):
    s = shrink(s)

    if all_happy_faces(s):
        for i, a in enumerate(ancestors):
            if a in cache and c - i < cache[a]:
                cache[a] = c - i
            elif a not in cache:
                cache[a] = c - i
            
        return costs.append(c)

    if s in ancestors:
        blacklist.append(s)
        return None # loop detected!

    for i in range(1, len(s) + 1):
        flipped = flip_first(s, i)

        if flipped in blacklist:
            continue

        elif flipped in cache:
            costs.append(c + cache[flipped] + 1)
            continue

        else:
            fn(flipped, c + 1, costs, ancestors + [s], blacklist, cache)
'''

def fn(s):
    s = shrink(s)
    c = 0
    cache = {'-+': 1, '+-': 2, '-': 1}
    while not all_happy_faces(s):
        c += cache[s[:2]]
        s = '+' + s[2:]
        s = shrink(s)
    return c

if __name__ == '__main__':
    import sys, re

    if len(sys.argv) < 2:
        sys.exit(-1)

    fname = sys.argv[1]

    with open(fname) as f:
        lines = f.read().strip().split('\n')

    ncases = int(lines[0])
    lines = lines[1:]

    for i in range(1, ncases + 1):
        s = lines[0]
        lines = lines[1:]

        costs = []
        print('Case #{}: {}'.format(i, fn(s)))
