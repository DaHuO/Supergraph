#!/usr/bin/python3.4

import sys
import math
from functools import reduce

def solve(l):
    flips = 0

    ll = len(l)

    while True:
        if '-' not in l:
            return flips
        t2 = len(l.rstrip('+'))
        l = flip(l, t2)
        flips += 1

def flip(l, n):
    r = ''
    for i in range(n):
        if l[i] == '+':
            r+= '-'
        else:
            r+= '+'
    return r + l[n:]

def main():
    nb = int(get_line())
    for case_id in range(1, nb + 1):
        line = get_line()
        l = solve(line)

        print('Case #%d: %d' %(case_id, l), file = o)

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

