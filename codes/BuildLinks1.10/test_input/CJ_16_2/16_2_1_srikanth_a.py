#!/usr/bin/python
import sys
from collections import Counter
from itertools import combinations, combinations_with_replacement

ipfile = sys.stdin
opfile = sys.stdout

T = int(ipfile.readline().strip())

digits = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
numbers = range(0,10)

d = {}
for l in range(1,11):
    d[l] = []
    for comb in combinations_with_replacement(numbers, l):
        totstr = ""
        comblist = list(comb)
        for x in comblist:
            s = digits[x]
            totstr += s
        cnt = Counter(totstr)
        d[l].append((comblist,cnt))

for t in xrange(1,T+1):
    ipstr = ipfile.readline().strip()
    ipctr = Counter(ipstr)
    found = False
    number = None
    for l in range(1,11):
        for x,cnt in d[l]:
            if cnt == ipctr:
                found = True
                number = "".join(map(str,sorted(x)))
                break
        if found:
            break
    
    opfile.write('Case #%d: %s\n' % (t,number))

                




