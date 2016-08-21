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
    s = [x for x in f.readline()]
    out = ""
    for j in s:
        if (len(out)==0):
            out += j
        elif (out[0]<=j):
            out = j + out
        else:
            out += j
    
    print "Case #%d: %s" % (i,out[:-1])