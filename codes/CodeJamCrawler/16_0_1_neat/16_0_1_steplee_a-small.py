#!/usr/bin/python2

import sys


def main():
    lines = []
    T = int(sys.stdin.readline())
    lines = [int(sys.stdin.readline()) for x in range(T)]

    [printCase(x+1, doit(y)) for (x,y) in enumerate(lines)]

def findDigits(n):
    i = 0
    ds = set()
    while n > 0:
        ds.add(n % 10)
        n = n/10
    return ds


def doit(N):
    seen = set()
    if N <= 0:
        return None
    for i in range(1,1000000):
        digits = findDigits(N*i)
        seen = seen.union(digits)
        if all( map(lambda x: x in seen, xrange(0,10)) ):
            break
    if i == 200:
            return None
    return i*N

def printCase(i, ans):
    if ans is not None:
        print ("Case #%d: %d"%(i,ans))
    else:
        print ("Case #%d: INSOMNIA"%i)


if __name__ == "__main__":
    main()

