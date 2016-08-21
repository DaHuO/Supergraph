#!/usr/bin/python3

import sys


def meow(n, i=1, seen=None):
    if n == 0:
        return 'INSOMNIA'
    if seen is None:
        seen = set()
    nn = n * i
    for c in str(nn):
        seen.add(c)
    if len(seen) == 10:
        return nn
    return meow(n, i + 1, seen)

if __name__ == '__main__':
    things = sys.argv[2:]
    for i, thing in enumerate(things, 1):
        print('Case #{}: {}'.format(i, meow(int(thing))))
