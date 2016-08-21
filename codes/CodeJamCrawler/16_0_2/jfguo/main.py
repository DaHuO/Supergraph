
import os
import sys
import glob
import subprocess
import random
import fileinput


next_line = 0
lines = [line.strip() for line in fileinput.input()]
def get_line():
    global next_line
    i = next_line
    next_line += 1
    return lines[i]

cache = {}

def rev(s):
    ans = ""
    for i in range(len(s) - 1, -1, -1):
        if s[i] == '+':
            ans += '-'
        else:
            ans += '+'
    return ans


def calc1(s):
    while s and s[-1] == '+':
        s = s[:-1]

    if not s:
        return 0

    if s in cache:
        return cache[s]

    if len(s) == 1:
        return 1

    ans = 1234567
    for i in range(1, len(s)):
        if s[i - 1] == '+':
            ns = rev(s[:i]) + s[i:]
            ns = rev(ns)
            t = calc1(ns) + 2
            if t < ans:
                ans = t

    if s[0] == '-':
        ns = rev(s)
        t = calc1(ns) + 1
        if t < ans:
            ans = t
    cache[s] = ans
    return ans

def calc():
    s = get_line()
    cache = {}
    return str(calc1(s))


T = int(get_line())
for i in range(1, T + 1):
    print('Case #%d: %s' % (i, calc()))
