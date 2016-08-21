#!/usr/bin/env python3
import sys
def q(n):
    s = set()
    if n == 0:
        return 'INSOMNIA'
    for i in range(1, 1000):
        s.update(d for d in str(i*n))
        if len(s) == 10:
            return str(i*n)

n = int(sys.stdin.readline())
for i in range(n):
    print("Case #%d: %s" % ((i+1), q(int(sys.stdin.readline()))))
