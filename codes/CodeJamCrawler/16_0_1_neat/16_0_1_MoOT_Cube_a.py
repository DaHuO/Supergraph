#!/usr/bin/env python

import sys

def numbers(k):
    acc = set()
    if(k==0):
        return acc
    while(k != 0):
        acc.add(k % 10)
        k = k // 10
    return acc


def sheep(i):
    k = 0
    acc = set()
    if(i == 0):
        return None
    while(len(acc) < 10):
        k += 1
        acc = acc.union(numbers(i * k))
    return k * i

if __name__ == "__main__":
    for (k, i) in enumerate([l.rstrip("\n") for l in sys.stdin.readlines()[1:]]):
        s = sheep(int(i))
        if(s):
            s = str(s)
        else:
            s = "INSOMNIA"
        print("Case #" + str(k + 1) + ": " + s)
