#!/usr/bin/python27

import sys

NUMS = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]

def solve(n):
    return str(n)

c = int(sys.stdin.readline())

results = []
for cn in range(c):
    n = int(sys.stdin.readline())
    numcp = []
    if n == 0:
        results.append('INSOMNIA')
        continue
    count = 0
    while len(numcp) < 10:
        n2 = n * (count + 1)
        remlist = solve(n2)
        for num in remlist:
            if not num in numcp:
                numcp.append(num)
        count += 1
    results.append(str(n2))

for i in range(len(results)):
    print "Case #%d: %s" % (i+1, results[i])
