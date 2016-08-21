#!/bin/python
import sys
input_filename, = sys.argv[1:]
input = open(input_filename)
assert input_filename.endswith('.in'), input_filename
output = open(input_filename[:-3]+'.out', 'w')
    
T = int(input.readline())

numbers = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

def solve():
    s = input.readline().strip()
    print s
    d = dict()
    for ss in numbers:
        for c in ss:
            d[c] = 0

    for c in s:
        d[c] = d[c] + 1

    print d

    dd = dict()
    
    dd[6] = d['X']
    for c in 'SIX':
        d[c] -= dd[6]
        
    dd[0] = d['Z']
    for c in 'ZERO':
        d[c] -= dd[0]

    dd[8] = d['G']
    for c in 'EIGHT':
        d[c] -= dd[8]

    dd[3] = d['H']
    for c in 'THREE':
        d[c] -= dd[3]

    dd[2] = d['W']
    for c in 'TWO':
        d[c] -= dd[2]

    dd[4] = d['U']
    for c in 'FOUR':
        d[c] -= dd[4]

    dd[5] = d['F']
    for c in 'FIVE':
        d[c] -= dd[5]

    dd[7] = d['V']
    for c in 'SEVEN':
        d[c] -= dd[7]

    dd[1] = d['O']
    for c in 'ONE':
        d[c] -= dd[1]

    dd[9] = d['I']
    for c in 'NINE':
        d[c] -= dd[9]

    for key, val in d.items():
        assert val == 0

    print dd
        
    s = ''
    for i in range(10):
        s += str(i) * dd[i]
    return s
        
for t in range(T):
    print >> output, 'Case #%s: %s' % (t+1,solve())

