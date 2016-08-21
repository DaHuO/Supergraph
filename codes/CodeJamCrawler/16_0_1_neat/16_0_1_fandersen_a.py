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

def solve (n):
    if n == 0:
        return "INSOMNIA"
    current = n
    seen = [False] * 10
    while True:
        for c in str(current):
            seen[int(c)] = True

        if all(seen):
            return current

        current += n

    return -9999


n = int(inp.readline())
for i in xrange(n):
    line = inp.readline().rstrip("\n")
    t = int(line)
    print("Case #" + str(i +1) +": " + str(solve(t)))
