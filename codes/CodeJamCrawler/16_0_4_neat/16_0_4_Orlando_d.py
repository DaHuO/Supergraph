#!/usr/bin/env python

t = int(raw_input())

for caseno in xrange(1, t+1):
    k, c, s = map(int, raw_input().split())
    chunk = k ** (c - 1)
    checks = k/2 + k%2
    if c == 1:
        checks = k
    if s < checks:
        print("Case #%d: IMPOSSIBLE" % caseno)
        continue
    if c == 1:
        print("Case #%d: %s" % (caseno, ' '.join(map(str, xrange(1, k+1)))))
        continue
    lim = k ** c
    indices = []
    offset = 0
    pos = 2
    for _ in xrange(checks):
        indices.append(min(offset + pos, lim))
        offset += 2*chunk
        pos += 2
    print("Case #%d: %s" % (caseno, ' '.join(map(str, indices))))
