from __future__ import division, print_function
from fileinput import input
from sys import setrecursionlimit
setrecursionlimit(20000)

try:
    xrange  # Python 2?
    range = xrange
except NameError:
    xrange = range
inp = input()



n = int(inp.readline())
for ii in xrange(n):
    line = inp.readline().rstrip("\n")
    s = line

    res = 1
    curr = s[0]
    for c in s:
        if c != curr:
            res += 1
            curr = c


    if s[-1] == '+':
        res -= 1
    print("Case #" + str(ii + 1) + ": " + str(res))
