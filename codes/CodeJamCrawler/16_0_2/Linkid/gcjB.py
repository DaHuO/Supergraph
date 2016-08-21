#!/usr/bin/env python
# -*- coding: utf-8 -*

"""GCJ 2016 Qualification Round: Problem B."""


def flip(stack, index):
    cara = '-' if stack[0] == '+' else '+'
    return (cara * (index + 1)) + stack[(index + 1):]


def solve(stack):
    sol = 0

    while stack.count('+') != len(stack):
        mem = None
        for i, pancake in enumerate(stack):
            if mem is None:
                mem = pancake
            if pancake != mem:
                i -= 1
                break
        stack = flip(stack, i)
        sol += 1

    return sol


if __name__ == "__main__":
    T = int(input())  # nb of test cases

    for x in range(T):
        S = input().strip()

        y = solve(S)
        print("Case #%d: %s" % (x + 1, y))
