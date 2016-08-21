#!/usr/bin/env python

import sys

sys.path.append("/Users/shanglin/projects/google_code_jam")
from gcj_boilerplate import *

initialize()
T = read_int()

def remove(p, numstr):
    for c in numstr:
        p = p.replace(c, '', 1)
    return p

for t in range(1, T + 1):
    p = read_line()
    digits = []
    num = 0
    print(p)
    while 'Z' in p:
        p = remove(p, 'ZERO')
        digits.append(0)
    print(p)
    while 'W' in p:
        p = remove(p, 'TWO')
        digits.append(2)
    while 'U' in p:
        p = remove(p, 'FOUR')
        digits.append(4)
    while 'X' in p:
        p = remove(p, 'SIX')
        digits.append(6)
    while 'G' in p:
        p = remove(p, 'EIGHT')
        digits.append(8)

    while 'O' in p:
        p = remove(p, 'ONE')
        digits.append(1)
    while 'T' in p:
        p = remove(p, 'THREE')
        digits.append(3)
    while 'F' in p:
        p = remove(p, 'FIVE')
        digits.append(5)
    while 'S' in p:
        p = remove(p, 'SEVEN')
        digits.append(7)
    print(p)
    while 'N' in p:
        p = remove(p, 'NINE')
        digits.append(9)

    digits = [str(c) for c in sorted(digits)]
    decoded = ''.join(digits)
    output(t, decoded)
end()