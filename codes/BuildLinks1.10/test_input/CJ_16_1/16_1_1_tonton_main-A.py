import logging
from collections import deque

# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.ERROR)

def solve(s):
    s = list(s)
    q = deque(s[0])
    for c in s[1:]:
        if c >= q[0]:
            q.appendleft(c)
        else:
            q.append(c)
    return "".join(q)


# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  s = raw_input()
  ans = solve(s)
  print "Case #{}: {}".format(i, ans)
  # check out .format's specification for more formatting options