#!/usr/bin/env python3

import sys

def solve(l):
    nowc = l[0]
    n=0
    for c in l:
        if nowc != c:
            n+=1
            nowc =c

    if nowc == '-':
        n += 1
    return n

def main():
    sys.stdin.readline()
    for i,l in enumerate(sys.stdin.readlines()):
        l = l[:-1]
        print("Case #{0}: {1}".format(i+1, solve(l)))

if __name__ == '__main__':
    main()
