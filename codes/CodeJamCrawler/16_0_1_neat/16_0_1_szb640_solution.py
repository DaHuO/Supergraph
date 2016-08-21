__author__ = 'bszikszai'

from io import *
import math

def simulate(n):
    if n == 0:
        return 'INSOMNIA'
    dgts = set()
    cn = n
    while(True):
        for digit in str(cn):
            dgts.add(digit)
        if len(dgts) == 10:
            return cn
        cn = cn + n

def solve(f):
    inp = int(f.readline().rstrip('\n\r '))
    return simulate(inp)

with open('input.txt', 'r') as f:
    with open('output.txt', 'wb') as g:
        cases = int(f.readline())
        for i in range(0, cases):
            solution = solve(f)
            print "Case #%s: %s" % (i+1, solution)
            g.write("Case #%s: %s\n" % (i+1, solution))