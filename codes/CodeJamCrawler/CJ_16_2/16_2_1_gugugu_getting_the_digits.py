from __future__ import division

import os
#import sys
#from math import log, floor, ceil, sqrt, pi
#from random import randint, choice, shuffle
from collections import Counter
#from heapq import heappush, heappop, heapify
#inf = 10**20

name = 'A-large.in'


def _solve(s):
    digits = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

    res = [None] * 10

    c = Counter(s)
    def subtract(digit, cnt):
        ss = digits[digit]
        for let in ss:
            c[let] = c[let] - cnt

    def getRes(digit, let):
        res[digit] = c[let]
        subtract(digit, res[digit])

    getRes(0, 'Z')
    getRes(6, 'X')
    getRes(2, 'W')
    getRes(8, 'G')
    getRes(4, 'U')
    getRes(5, 'F')
    getRes(1, 'O')
    getRes(3, 'T')
    getRes(7, 'V')
    getRes(9, 'I')

    assert(sum(c[k] for k in range(10)) == 0)

    num = []
    for d in range(10):
        for i in range(res[d]):
            num.append(d)

    return num

#digits = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
#import random
#import sys
#def test():
#    for _ in range(1000):
#        sol = tuple(sorted([random.randint(0,9) for i in range(2000)]))
#        l = list(''.join([digits[digit] for digit in sol]))
#        random.shuffle(l)
#        inp = ''.join(l)
#        res = tuple(_solve(inp))
#        assert(res == sol)
#        print(res)
#test()
#sys.exit()

def solve(*args, **kwargs):
    res = _solve(*args, **kwargs)
    return ''.join(map(str, res))

inp_path = '/home/mama/Downloads/%s'%name
if os.path.isfile(inp_path):
    os.system('mv %s .' % inp_path)
inp_file = open(name)
out_file = open('%s.out'%name, 'w')
cases = int(inp_file.readline())
for caseno in range(cases):
    s = inp_file.readline().strip()
    res = solve(s)
    print(caseno, res)
    print('---')
    out_file.write('Case #%d: %s\n'%((caseno+1), res))
    out_file.flush()
out_file.close()









