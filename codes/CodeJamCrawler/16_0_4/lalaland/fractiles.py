# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 20:32:41 2016

@author: avishay
"""

import time

def next_place(k, c, remaining):
    index = 0
    for i in range(c):
        next_cover = 1 if len(remaining) == 0 else remaining.pop(0)
        index += k**(c-i-1) * (next_cover - 1)
    return index + 1, remaining

def solve(lines):
    K, C, S = map(int, lines[0].split())
    if S*C < K:
        return 'IMPOSSIBLE'
    remaining = list(range(1, K+1))
    res = []
    while len(remaining) > 0:
        d, remaining = next_place(K, C, remaining)
        res.append(d)
    return ' '.join(map(str, res))

lines = open('/home/avishay/Downloads/cj/fractiles/D-large.in').readlines()
num_cases = int(lines[0])
lines_per_case = 1
start = time.time()
o = open('/home/avishay/Downloads/cj/fractiles/large-out', 'w')

for i in range(num_cases):
    res = solve(lines[i*lines_per_case+1:(i+1)*lines_per_case+1])
    print('Case #%d: %s' % (i+1, res))
    o.write('Case #%d: %s\n' % (i+1, res))

o.close()
print('runtime=%.2f' % (time.time() - start))