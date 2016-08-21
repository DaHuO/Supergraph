#!/usr/bin/env python3

def readint():
    return int(input())

def readints():
    return map(int, input().split())

def readline():
    return str(input())

T = readint()
for case in range(T):
    N = readint()
    k = 0
    s = set()
    while len(s) < 10 and k<2**20:
        s.update(list(str((k+1)*N)))
        k += 1
    result = str(k*N)
    if k>=2**20:
        result = "INSOMNIA"





    print("Case #%d: %s" % (case+1, result))
