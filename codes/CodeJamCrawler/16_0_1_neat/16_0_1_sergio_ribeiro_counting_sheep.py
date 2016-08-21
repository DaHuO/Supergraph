#!python
# http://code.google.com/codejam/contest/dashboard?c=32016#s=p0
import sys
from optparse import OptionParser
from collections import deque
import math
import operator
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

def removeDigits(N,REMAINING):
    for digit in str(N):
        if int(digit) in REMAINING:
            REMAINING.remove(int(digit))
    return REMAINING

T = int(f.readline())

for i in range(1,T+1):
    n = int(f.readline())
    if(n==0):
        print "Case #%d: INSOMNIA" % (i)
    else:
        remaining=[0,1,2,3,4,5,6,7,8,9]
        multiplier = 1
        lastResult = multiplier*n
        remaining = removeDigits(lastResult,remaining)
        while(len(remaining)):
            multiplier+=1
            lastResult=multiplier*n
            remaining = removeDigits(lastResult,remaining)

        print "Case #%d: %d" % (i,lastResult)
