#!/usr/bin/env python3

################################################################################

def read_int():
    return int(input())


def read_words():
    return input().split()


def parse(f):
    return [f(x) for x in read_words()]


def read_ints():
    return parse(int)


def read_floats():
    return parse(float)


################################################################################

def tochars(n):
    return { c for c in str(n) }

def solve(n):
    if n == 0:
        return "INSOMNIA"
    all = tochars(1234567890)
    s   = tochars(n)
    acc = n
    while s != all:
        acc += n
        s = s.union(tochars(acc))
    return acc

import sys
#sys.stdin = open("example.in")
for C in range(read_int()):
    R = solve(read_int())
    print("Case #{}: {}".format(C + 1, R))
