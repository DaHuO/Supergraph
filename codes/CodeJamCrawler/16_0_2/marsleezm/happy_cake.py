#!/usr/bin/env python3

import sys


def getresult(style):
    prev = None
    flip = 0
    for c in style:
        if c == '\n':
            break
        if prev == None:
            prev = c
        else:
            if prev == c:
                continue
            else:
                flip += 1
                prev = c
    if prev == '-':
        flip += 1
    return str(flip) 

if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    t = int(f.readline())
    for ind in range(1,t+1):
        style = f.readline()
        result = getresult(style)
        print("Case #"+str(ind)+": "+result)
