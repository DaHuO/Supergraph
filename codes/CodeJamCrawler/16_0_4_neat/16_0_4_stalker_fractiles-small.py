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

def solve(k,c,s):
    if s != k:
        raise "Not a small problem"
    bs = k ** (c-1)
    return " ".join([ str(1 + i*bs) for i in range(k)])

for case in range(read_int()):
    [K,C,S] = read_ints()
    R = solve(K,C,S)
    print("Case #{}: {}".format(case + 1, R))
