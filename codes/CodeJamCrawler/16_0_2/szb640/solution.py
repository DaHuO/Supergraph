__author__ = 'bszikszai'

from io import *
import math

def simulate(n):
    flip = 0
    for i in range(len(n) - 1, -1, -1):
        if not n[i]:
            flip = flip + 1
            for j in range(0, i + 1):
                n[j] = not n[j]
    return flip

def solve(f):
    inp = [(ch == '+') for ch in f.readline().rstrip('\n\r ')]
    return simulate(inp)

with open('input.txt', 'r') as f:
    with open('output.txt', 'wb') as g:
        cases = int(f.readline())
        for i in range(0, cases):
            solution = solve(f)
            print "Case #%s: %s" % (i+1, solution)
            g.write("Case #%s: %s\n" % (i+1, solution))