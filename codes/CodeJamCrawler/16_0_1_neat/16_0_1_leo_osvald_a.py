#!/usr/bin/env python3

import sys

def solve(n):
    if n == 0:
        return "INSOMNIA"

    x = n
    seen = set()
    while len(seen) <= 9:
        last = x
        seen |= set(str(x))
        x += n
    return last

def main(args=sys.argv):
    t = int(sys.stdin.readline())
    for i in range(t):
        n = int(sys.stdin.readline())
        print("Case #%d:" % (i + 1), end=" ")
        print(solve(n))

    return 0

if __name__ == '__main__': sys.exit(main())
