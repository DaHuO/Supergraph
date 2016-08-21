# -*- coding: utf-8 -*-


def solve(n):
    if(n == 0):
        return "INSOMNIA"
    n0 = n
    d = {}
    while True:
        for i in str(n):
            d[int(i)] = True
        if len(d) == 10:
            return str(n)
        else:
            n += n0


t = int(input())
for i in range(t):
    n = int(input())
    print("Case #" + str(i+1) + ": " + solve(n))
