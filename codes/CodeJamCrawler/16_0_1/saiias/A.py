#! /usr/bin/env python
# -*- coding: utf-8 -*-


def solve(n):
    if n == 0:
        return "INSOMNIA"

    ret = set()
    i = 1

    while True:

        temp = n * i
        for j in str(temp):
            ret.add(j)


        if len(ret) == 10:
            return str(temp)

        i = i + 1


def main():
    N = int(raw_input())
    for i in xrange(N):
        inp = int(raw_input())
        ans = solve(inp)
        print "Case #"+str(i+1) + ": " + str(ans)

    return 0

if __name__ == "__main__":
    main()
