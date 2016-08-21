
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


def calc():
    K, C, S = [int(i) for i in get_line().split()]
    p = K ** (C - 1)
    vals = [1]
    for i in range(S - 1):
        vals.append(vals[-1] + p)
    return ' '.join([str(i) for i in vals])

T = int(get_line())
for i in range(1, T + 1):
    print('Case #%d: %s' % (i, calc()))
