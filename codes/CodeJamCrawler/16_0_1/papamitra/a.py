#!/usr/bin/env python3

import sys

def solve(n):
    if n==0: return 'INSOMNIA'

    r = n
    s=set()

    while True:
        s.update(set(str(r)))
        if len(s) == 10: return r
        r += n

def main():
    sys.stdin.readline()
    for i, n in enumerate(sys.stdin.readlines()):
        print("Case #{0}: {1}".format(i+1, solve(int(n))))

if __name__ == '__main__':
    main()
