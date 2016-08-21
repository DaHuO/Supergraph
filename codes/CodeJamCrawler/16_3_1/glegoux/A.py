#!/usr/bin/env python3

import sys

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def f(N, Ps):
    plan = []
    while not nobody(Ps):
        i1 = find(Ps)
        decrement(i1, Ps)
        names = alphabet[i1]
        i2 = find(Ps)
        decrement(i2, Ps)
        if check(Ps):
            names += alphabet[i2]
        else:
            increment(i2, Ps)
        plan.append(names)
    return plan

def nobody(Ps):
    for p in Ps:
        if p != 0:
            return False
    return True

def find(Ps):
    m = 0
    im = 0
    for i, p in enumerate(Ps):
        if p > m:
            m = p
            im = i
    return im

def has_majority(i, Ps):
    return Ps[i] > sum(Ps)/2

def check(Ps):
    for i, p in enumerate(Ps):
        if Ps[i] > sum(Ps)/2:
            return False
    return True


def decrement(i, Ps):
    if Ps[i] > 0:
        Ps[i] -= 1

def increment(i, Ps):
        Ps[i] += 1

def print_answer(n, result):
    res = ""
    if type(result) in [list, tuple]:
        res = " ".join(map(str, result))
    elif type(result) == int:
        res = str(result)
    elif type(result) == str:
        res = result
    print("Case #{}: {}".format(n, res))

def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        Ps = list(map(int, input().split(' ')))
        #print(N, Ps)
        print_answer(t + 1, f(N, Ps))

if __name__ == "__main__":
    main()
