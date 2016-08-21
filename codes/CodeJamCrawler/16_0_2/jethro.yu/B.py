#!/usr/bin/python
import sys
from string import maketrans
intab = "-+"
outtab = "+-"
trantab = maketrans(intab, outtab)


def flip(stack, i):
    return stack[i::-1].translate(trantab) + stack[i+1::]

def solve(p):
    i = 0
    #last = len(p)
    p = p[:p.rfind('-') + 1:]
    #print p + '+' * (last - len(p))
    while len(p) != 0:
        if p[0] == '-':
            at = len(p)-1
        if p[0] == '+':
            at = p.rfind('+')
        p = flip(p, at)
        #print at+1, p + '+' * (last - len(p))
        p = p[:p.rfind('-')+1:]
        i += 1
    return i

#solve("--++")

for i in range(1, int(raw_input())+1):
    print "Case #{}:".format(i), solve(raw_input())
sys.exit()
