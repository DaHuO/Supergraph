#!/usr/bin/python
import sys

T = int(sys.stdin.readline().strip())
for tt in range(T):
    K, C, S = map(int, sys.stdin.readline().strip().split())
    assert K == S
    pos = [1 + i * K ** (C - 1) for i in range(K)]
    print 'Case #%d: %s' % (tt + 1, ' '.join(map(str, pos)))
