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
for i in xrange(n):
    line = inp.readline().rstrip("\n")
    k, c, s = map(int, line.split())
    sol = []
    if s != k:
        print(line)
        print(s, k)
        print("wrong: " + str(i))
    jump = k**(c-1)
    for ii in range(k):
        sol.append(1+ii*jump)
    print("Case #" + str(i +1) + ": " + " ".join(map(str, sol)))
