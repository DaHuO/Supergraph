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

def flip(N,REMAINING):
    if(REMAINING[0] == '-'):
        return N*"+" + REMAINING[N+1:len(REMAINING)]
    else:
        return N*"-" + REMAINING[N+1:len(REMAINING)]

T = int(f.readline())

for i in range(1,T+1):
    s = f.readline()
    numberOfFlips = 0
    while(s.count('-')>0):
        firstOcurrenceIndex = s.find('-')
        if firstOcurrenceIndex == 0:
            if(s.count('+') == 0):
                s = flip(len(s),s)
                numberOfFlips += 1
            else:
                firstOcurrenceIndex = s.find('+')
                s = flip(firstOcurrenceIndex-1,s)
                numberOfFlips += 1
        else:
            s = flip(firstOcurrenceIndex-1,s)
            numberOfFlips += 1

    print "Case #%d: %d" % (i,numberOfFlips)
