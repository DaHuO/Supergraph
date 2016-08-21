#!/usr/bin/python3
import sys
# import math
import fractions
sys.setrecursionlimit(1000000)
DEBUG = 0


def rl(convert='', a=False):
    line = sys.stdin.readline().split()
    for i, c in enumerate(convert):
        if c == 'i':
            line[i] = int(line[i])
        elif c == 's':
            pass
        elif c == 'f':
            line[i] = float(line[i])
    if not a and len(line) == 1:
        return line[0]
    return line


def gcd(*args):
    if len(args) == 0:
        return 0
    g = args[0]
    for i in range(1, len(args)):
        g = fractions.gcd(g, args[i])
    return g


def lcm(*args):
    if len(args) == 0:
        return 0
    g = args[0]
    for i in range(1, len(args)):
        g *= args[i]
    return g / gcd(*args)


def avg(a):
    return sum(a) / len(a)


def debug(*args, **kwargs):
    level = 1
    if 'level' in kwargs:
        level = kwargs.pop('level')
    if DEBUG >= level:
        print(*args, **kwargs)
        # pass


def o(i, x):
    print('Case #{}: {}'.format(i + 1, x))
# --------------------------------------------------------------------#


def reverse_complement(pile):
    return map(lambda p: '-' if p == '+' else '+', reversed(pile))


def flip(pile, n):
    pile[:n] = reverse_complement(pile[:n])
    debug('flip', n, pile)


tc = range(rl('i'))
for t in tc:
    pile = list(rl('s'))
    debug(pile)
    n = 0
    for i in reversed(range(len(pile))):
        if pile[i] == '-':
            top_ok = 0
            while (top_ok < len(pile) and pile[top_ok] == '+'):
                top_ok += 1
            if top_ok > 0:
                flip(pile, top_ok)
                n += 1
            flip(pile, i + 1)
            n += 1
    o(t, n)
