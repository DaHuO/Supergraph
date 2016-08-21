#!python
import sys
from optparse import OptionParser
from collections import deque
import math
import operator
import itertools
import re
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

nums = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]


T = int(f.readline())
for i in range(1,T+1):
    line = f.readline()
    out = ""
    
    while "Z" in line:
        out += "0"
        line = re.sub("Z","",line,count=1)
        line = re.sub("E","",line,count=1)
        line = re.sub("R","",line,count=1)
        line = re.sub("O","",line,count=1)

    while "W" in line:
        out += "2"
        line = re.sub("T","",line,count=1)
        line = re.sub("W","",line,count=1)
        line = re.sub("O","",line,count=1)

    while "U" in line:
        out += "4"
        line = re.sub("F","",line,count=1)
        line = re.sub("O","",line,count=1)
        line = re.sub("U","",line,count=1)
        line = re.sub("R","",line,count=1)

    while "X" in line:
        out += "6"
        line = re.sub("S","",line,count=1)
        line = re.sub("I","",line,count=1)
        line = re.sub("X","",line,count=1)

    while "G" in line:
        out += "8"
        line = re.sub("E","",line,count=1)
        line = re.sub("I","",line,count=1)
        line = re.sub("G","",line,count=1)
        line = re.sub("H","",line,count=1)
        line = re.sub("T","",line,count=1)

    while "T" in line:
        out += "3"
        line = re.sub("T","",line,count=1)
        line = re.sub("H","",line,count=1)
        line = re.sub("R","",line,count=1)
        line = re.sub("E","",line,count=1)
        line = re.sub("E","",line,count=1)

    while "O" in line:
        out += "1"
        line = re.sub("O","",line,count=1)
        line = re.sub("N","",line,count=1)
        line = re.sub("E","",line,count=1)

    while "F" in line:
        out += "5"
        line = re.sub("F","",line,count=1)
        line = re.sub("I","",line,count=1)
        line = re.sub("V","",line,count=1)
        line = re.sub("E","",line,count=1)

    while "I" in line:
        out += "9"
        line = re.sub("N","",line,count=1)
        line = re.sub("I","",line,count=1)
        line = re.sub("N","",line,count=1)
        line = re.sub("E","",line,count=1)

    while "S" in line:
        out += "7"
        line = re.sub("S","",line,count=1)
        line = re.sub("E","",line,count=1)
        line = re.sub("V","",line,count=1)
        line = re.sub("E","",line,count=1)
        line = re.sub("N","",line,count=1)

    out = ''.join(sorted(out))
    print "Case #%d: %s" % (i,out)