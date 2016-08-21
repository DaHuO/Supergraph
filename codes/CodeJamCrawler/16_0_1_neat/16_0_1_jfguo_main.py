
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
    v = int(get_line())
    if v == 0:
        return "INSOMNIA"

    see = 0
    cur = 0
    while see != (1<<10) - 1:
        cur += v
        s = str(cur)
        for c in s:
            see |= 1 << (ord(c) - ord('0'))

    return str(cur)


T = int(get_line())
for i in range(1, T + 1):
    print('Case #%d: %s' % (i, calc()))
