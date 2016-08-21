#!/usr/bin/python
import numpy as np

def read_file():
    f = open('A-large.in', 'r')
    return f.read().splitlines()

def calculate(line):
    r = ''
    list_c = list(line)

    while len(list_c) > 0:
        if 'Z' in list_c:
            r += '0'
            for c in 'ZERO':
                list_c.remove(c)
            continue

        if 'X' in list_c:
            r += '6'
            for c in 'SIX':
                list_c.remove(c)
            continue

        if 'W' in list_c:
            r += '2'
            for c in 'TWO':
                list_c.remove(c)
            continue

        if 'U' in list_c:
            r += '4'
            for c in 'FOUR':
                list_c.remove(c)
            continue

        if 'G' in list_c:
            r += '8'
            for c in 'EIGHT':
                list_c.remove(c)
            continue

        x = 'ONE'
        if check(x, list_c):
            r += str(1)
            for c in x:
                list_c.remove(c)
            continue

        x = 'THREE'
        if check(x, list_c):
            r += str(3)
            for c in x:
                list_c.remove(c)
            continue

        x = 'FIVE'
        if check(x, list_c):
            r += str(5)
            for c in x:
                list_c.remove(c)
            continue

        x = 'SEVEN'
        if check(x, list_c):
            r += str(7)
            for c in x:
                list_c.remove(c)
            continue

        x = 'NINE'
        if check(x, list_c):
            r += str(9)
            for c in x:
                list_c.remove(c)
            continue


    return ''.join(sorted(r))


def check(s, test):
    for c in s:
        if not c in test:
            return False
    return True

lines = read_file()
t = int(lines[0])  # read a line with a single integer
for i in xrange(1, t + 1):
    result = calculate(lines[i])
    # print lines[i]
    print "Case #{}: {}".format(i, result)
