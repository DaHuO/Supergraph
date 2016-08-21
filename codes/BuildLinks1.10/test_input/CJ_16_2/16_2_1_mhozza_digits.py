#!/usr/bin/python3
import sys
from collections import defaultdict
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

DIGITS = (
    "ZERO", "ONE", "TWO", "THREE", "FOUR",
    "FIVE", "SIX", "SEVEN", "EIGHT", "NINE",
)

unique1 = {
    'Z': 0,
    'W': 2,
    'U': 4,
    'X': 6,
    'G': 8,
}

unique2 = {
    'H': 3,
    'F': 5,
    'S': 7,
}

unique3 = {
    'O': 1,
    'I': 9,
}

tc = rl('i')
for t in range(tc):
    s = rl('s')
    sl = defaultdict(int)

    for l in s:
        sl[l] += 1
    sl = dict(sl)

    digits = []

    while set(sl.keys()) & set(unique1):
        new_digits = [unique1[l] for l in set(sl.keys()) & set(unique1)]
        digits += new_digits
        for d in new_digits:
            for l in DIGITS[d]:
                sl[l] -= 1
                if sl[l] == 0:
                    del sl[l]

    while set(sl.keys()) & set(unique2):
        new_digits = [unique2[l] for l in set(sl.keys()) & set(unique2)]
        digits += new_digits
        for d in new_digits:
            for l in DIGITS[d]:
                sl[l] -= 1
                if sl[l] == 0:
                    del sl[l]

    while set(sl.keys()) & set(unique3):
        new_digits = [unique3[l] for l in set(sl.keys()) & set(unique3)]
        digits += new_digits
        for d in new_digits:
            for l in DIGITS[d]:
                sl[l] -= 1
                if sl[l] == 0:
                    del sl[l]

    o(t, ''.join(str(x) for x in sorted(digits)))
