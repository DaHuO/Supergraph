#!python
#Sergio Schirmer Almenara Ribeiro
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

def returnWinner(s):
    s = s.replace("\n","")
    winner = str()
    for c in s:
        if len(winner)>0:
            if c>=winner[0]:
                winner = c+winner
            else:
                winner = winner+c
        else:
            winner = c
    return winner

T = int(f.readline())

for i in range(1,T+1):
    s = f.readline()
    winner = returnWinner(s)
    print "Case #%d: %s" % (i,winner)
