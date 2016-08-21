#! /usr/bin/python
# kmwho
# CodeJam 2016 Qualification Round

from __future__ import print_function

def __del():
    input()
    int(input())
    map(int,input().split())

def solvecase(N):
    if N == 0:
        return "INSOMNIA"
    alldigits = set(str(d) for d in range(10))
    seen      = set()
    i = 1
    while True:
        x = i*N
        digits = set( str(x) )
        seen.update(digits)
        if seen == alldigits:
            break
        i  += 1
    return str(i*N)

def solve():
    T = int(input())
    for t in range(T):
        N = int(input())
        res = solvecase(N)
        print("Case #" + str(t+1) + ": " + str(res) )

def main():
    solve()


main()
