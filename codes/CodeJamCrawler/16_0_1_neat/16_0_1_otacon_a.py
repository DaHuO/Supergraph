#!/usr/bin/python3.4

import sys
import math
from functools import reduce

def solve(n):
    seen = [False] * 10
    i = 0
    while True:
        if False not in seen:
            return n * i

        i += 1
        digits = str(n*i)
        for j in digits:
            seen[int(j)] = True
        if i >100000:
            return None

    return 0

def main():
    nb = int(get_line())
    for case_id in range(1, nb + 1):
        n = int(get_line())

        ret = solve(n)
        if ret == None:
            l = 'INSOMNIA'
        else:
            l = str(ret)
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

