import numpy as np
from sys import argv

def solve(s):
    res = 0
    s += '+'
    for i in range(len(s) - 1):
        if s[i] != s[i+1]:
            res += 1
    return res
    
    
t = int(input())

for i in range(1, t+1):
    print("Case #%d: %d" % (i, solve(input())))
