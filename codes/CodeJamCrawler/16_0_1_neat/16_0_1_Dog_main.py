#! /usr/bin/env python3
import re
import sys

def solve(n):
    if n == 0: return "INSOMNIA"
    s = set('0123456789') 
    i = 0
    while s:
        i += 1
        list(map(s.discard, str(i*n)))
    return i*n


with open(sys.argv[1]) as f:
    content = f.read()

numbers = list(map(int, re.findall(r'\d+', content)))[1:]
for (c, n) in enumerate(numbers, 1):
    print("Case #{}:".format(c), solve(n))
