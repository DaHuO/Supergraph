
import os
import sys
import glob
import subprocess
import random
import fileinput


next_line = 0
lines = [line.strip() for line in fileinput.input()]
def get_line():
    global next_line
    i = next_line
    next_line += 1
    return lines[i]


def test(v, b):
    p = 0
    for i in range(N - 1, -1, -1):
        p *= b
        if v & (1<<i):
            p += 1
    
    d = 2
    if d != p and p % d == 0:
        return 2

    d = 3
    while d * d <= p and d <= 100:
        if p % d == 0:
            return d
        d += 2
    return None


T = int(get_line())
for i in range(1, T + 1):
    print('Case #%d:' % i)
    N, J = get_line().split()
    N = int(N)
    J = int(J)

    x = 0
    while True:
        v = (1 << (N - 1)) + 1 + (x << 1)
        x += 1

        fail = False
        ds = []
        for b in range(2, 11):
            d = test(v, b)
            if not d:
                fail = True
            ds.append(d)
        if fail:
            continue

        bb = []
        for i in range(N - 1, -1, -1):
            if v & (1<<i):
                bb.append(1)
            else:
                bb.append(0)
        print ''.join([str(i) for i in bb]),
        for d in ds:
            print d,
        print

        J -= 1
        if J == 0:
            break
