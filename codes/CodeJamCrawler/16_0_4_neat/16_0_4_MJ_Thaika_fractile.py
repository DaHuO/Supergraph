#!python
import sys
from optparse import OptionParser
from collections import deque
import math
import operator
import itertools
usage = "usage: %prog input"
parser = OptionParser(usage=usage)
(options, args) = parser.parse_args()
if args:
    if args[0] == "-":
        f = sys.stdin
    else:
        f = open(args[0])
elif not sys.stdin.isatty():
    f = sys.stdin
else:
    parser.error("Need input from file or stdin")

T = int(f.readline())
for i in range(1,T+1):
    k,c,s = [int(x) for x in f.readline().split()]
    
    prev = 0
    start = 1
    for j in range(1,min(k,c)):
        prev = (k*prev)+1
        start += prev

    if (k>c):
        ans = [x for x in range(start,start+(k-c)+1)]
    else:
        ans = [start]

    out = ' '.join(map(str, ans)) 
    if (len(ans)>s):
        print "Case #%d: IMPOSSIBLE" % i
    else:
        print "Case #%d: %s" % (i,out)