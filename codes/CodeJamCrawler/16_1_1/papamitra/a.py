#!/usr/bin/env python3

import sys

def solve(s):
    solv=[s[0]]
    for c in s[1:]:
        if solv[0] <= c:
            solv.insert(0,c)
        else:
            solv.append(c)
    return ''.join(solv)

def main():
    sys.stdin.readline()
    for i,l in enumerate(sys.stdin.readlines()):
        l = l[:-1]
        print("Case #{0}: {1}".format(i+1, solve(l)))

if __name__ == '__main__':
    main()
