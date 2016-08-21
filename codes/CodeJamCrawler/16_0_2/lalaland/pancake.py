# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import re

cache = {}

def switch(line):
    res = []
    for c in line:
        res.append('-' if c == '+' else '+')
    return ''.join(res)

def rec_solve(trail, line):
    if '-' not in line:
        return 0
    line = re.sub('-+', '-', line)
    line = re.sub('\++', '+', line)
    if line in trail:
        return 10**10
    if line in cache:
        cache[line]
    best = len(line)+1
    for i in range(1, len(line)):
        temp_line = switch(line[:i][::-1])+line[i:]
        t = rec_solve(trail + [line], temp_line)
        cache[temp_line] = t
        if t < best:
            best = t
            if best == 0:
                return 1
    return best+1
    
def solve(lines):
    line = lines[0]
    return rec_solve([], str(line))

lines = open('/home/avishay/Downloads/cj/pancake/B-small-attempt0.in').readlines()
num_cases = int(lines[0])
lines_per_case = 1
o = open('/home/avishay/Downloads/cj/pancake/sample-out', 'w')
for i in range(num_cases):
    res = solve(lines[i*lines_per_case+1:(i+1)*lines_per_case+1])
    print('Case #%d: %s' % (i+1, res))
    o.write('Case #%d: %s\n' % (i+1, res))

o.close()