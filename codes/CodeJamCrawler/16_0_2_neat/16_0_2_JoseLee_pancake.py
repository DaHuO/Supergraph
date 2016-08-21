from math import *
import sys

PLUS = 1
MINUS = -1

def is_plus(s):
    if s == '+':
        return PLUS
    else:
        return MINUS

def solveit(S):

    len_s = len(S)
    pre = PLUS
    flip_count = 0
    for i in range(len_s-1, -1, -1):
        if is_plus(S[i]) != pre:
            flip_count += 1
            pre = is_plus(S[i])

    return flip_count

if __name__ == '__main__':
    script, inpf = sys.argv
    maxtest = 0

    with open(inpf, 'r') as inp:
        lines = inp.readlines()

    lines = [(line.rstrip('\n')) for line in lines]
    maxtest = int(lines[0])
    tests = lines[1:]

    for testn in range(0, maxtest):
        result = solveit(tests[testn])
        print "Case #{0}: {1}".format(testn+1, result)

