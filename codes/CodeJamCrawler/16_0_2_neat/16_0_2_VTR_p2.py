__author__ = 'VTR'
import sys


assert(len(sys.argv) > 1)


def done(s):
    count = 0
    for c in s:
        if c == '+':
            count += 1
    return count == len(s)


def aswap(s):
    res = ''
    for i in range(len(s)):
        if s[i] == '+':
            res += '-'
        else:
            res += '+'
    return res


def swaps(s):
    moves = 0
    while not done(s):
        moves += 1
        for i in range(len(s), 0, -1):
            if s[i - 1] == '-':
                s = aswap(s[:i]) + s[i:]
                break
    return moves


with open(sys.argv[1], 'r') as fp:
    t = int(fp.readline())
    for i in range(1, t+1):
        s = fp.readline().strip()
        print 'Case #'+str(i)+': ' + str(swaps(s))