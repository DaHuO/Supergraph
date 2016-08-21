#!/usr/bin/python3.4

import sys
import math
from functools import reduce

def solve(k, c, s):
    l=[]

    if k != s:
        return None

    for i in range(s):
        p = 0
        for j in range(c):
            p += i * k**(j)

        l.append(p + 1)
    return l

def main():
    nb = int(get_line())
    for case_id in range(1, nb + 1):
        k, c, s = [int(i) for i in get_line().split(' ')]

        ret = solve(k, c, s)
        if ret == None:
            l = 'IMPOSSIBLE'
        else:
            l = ' '.join([str(i) for i in ret])
        print('Case #%d: %s' %(case_id, l), file = o)

def get_line():
    return f.readline().strip()

def open_files():
    if len(sys.argv) == 1:
        f = sys.stdin
        o = sys.stdout

    if len(sys.argv) == 2:
        f = open(sys.argv[1], 'r')
        o = sys.stdout

    if len(sys.argv) == 3:
        f = open(sys.argv[1], 'r')
        o = open(sys.argv[2], 'w')

    return (f, o)

if __name__ == "__main__":
    (f, o) = open_files()
    main()

