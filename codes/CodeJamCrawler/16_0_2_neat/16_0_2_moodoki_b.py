#!/usr/bin/env python

import sys

def main():
    """docstring for main"""
    filename = sys.argv[1]
    f = open(filename)
    T = int(f.readline())
    for i in range(T):
        s = solve(f.readline())
        print "Case #"+str(i+1)+":", s
    f.close()

def solve( instr ):
    p = instr.rstrip()
    flipcnt = 0
    while not allup(p):
        s = p[0]
        if s == '+':
            ss = '-'
        else:
            ss = '+'
        try:
            oppi = p.index(ss)
            p = oppi*ss + p[oppi:]
        except ValueError:
            p = ss * len(p)
        flipcnt = flipcnt + 1
    return flipcnt



def allup(p):
    if p[0] == '+' and len(set(p)) == 1:
        return True
    else:
        return False


if __name__ == '__main__':
    main()
