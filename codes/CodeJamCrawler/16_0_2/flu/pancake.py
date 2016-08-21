#!/usr/bin/env python


def is_happy(stack):
    return not '-' in stack

def flip(stack):
    first = stack[0]
    if first == '+':
        new_sym = '-'
    else:
        new_sym = '+'
    pos = 0
    for pos,s in enumerate(stack):
        if s != first:
            break
        stack[pos] = new_sym
    return stack

def task(stack):
    stack = list(stack)
    i = 0
    while not is_happy(stack):
        stack = flip(stack)
        i += 1
    return i


if __name__ == '__main__':
    T = int(input())
    i = 1
    while T > 0:
        res = task(input().strip())
        print("Case #{0}: {1}".format(i, res))
        i += 1
        T -= 1
