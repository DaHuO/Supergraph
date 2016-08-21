#!/usr/bin/python

import sys
from collections import defaultdict

f = open("large.in","rb")
t = int(f.readline())
global res

def solve(s):
    res = defaultdict(int)
    count = defaultdict(int)
    for i in s:
        count[i]+=1

    if 'Z' in count:
        res[0] = count['Z']
        count['E'] -= count['Z']
        count['R'] -= count['Z']
        count['O'] -= count['Z']
        count['Z'] = 0

    if 'W' in count:
        res[2] = count['W']
        count['T'] -= count['W']
        count['O'] -= count['W']
        count['W'] = 0

    if 'U' in count:
        res[4] = count['U']
        count['F'] -= count['U']
        count['O'] -= count['U']
        count['R'] -= count['U']
        count['U'] = 0

    if 'X' in count:
        res[6] = count['X']
        count['S'] -= count['X']
        count['I'] -= count['X']
        count['X'] = 0

    if 'G' in count:
        res[8] = count['G']
        count['E'] -= count['G']
        count['I'] -= count['G']
        count['H'] -= count['G']
        count['T'] -= count['G']
        count['G'] = 0

    if 'F' in count and count['F'] > 0:
        res[5] = count['F']
        count['I'] -= count['F']
        count['V'] -= count['F']
        count['E'] -= count['F']
        count['F'] = 0

    if 'V' in count and count['V'] > 0:
        res[7] = count['V']
        count['S'] -= count['V']
        count['E'] -= 2*count['V']
        count['N'] -= count['V']
        count['V'] = 0

    if 'O' in count and count['O'] > 0:
        res[1] = count['O']
        count['N'] -= count['O']
        count['E'] -= count['O']
        count['O'] = 0

    if 'R' in count and count['R'] > 0:
        res[3] = count['R']
        count['T'] -= count['R']
        count['H'] -= count['R']
        count['E'] -= 2*count['R']
        count['R'] = 0

    if 'I' in count and count['I'] > 0:
        res[9] = count['I']
        count['N'] -= 2*count['I']
        count['E'] -= count['I']
        count['I'] = 0

    for v in count.values():
        if v > 0:
            print "ERROR: "
    return res

for i in range(t):
    s = f.readline().strip()
    out = solve(s)
    res = ""
    for k,v in sorted(out.iteritems()):
        for ii in range(v):
            res += str(k)
    print "Case #%s:" % (i+1), res
