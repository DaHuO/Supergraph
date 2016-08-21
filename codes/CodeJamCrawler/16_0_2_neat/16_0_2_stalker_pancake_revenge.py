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

def solve(p):
    result = 0
    for i in range(len(p)-1):
        if p[i] != p[i+1]:
            result += 1
    return result



for C in range(read_int()):
    I = input().strip()
    R = solve(I + '+')
    print("Case #{}: {}".format(C + 1, R))
