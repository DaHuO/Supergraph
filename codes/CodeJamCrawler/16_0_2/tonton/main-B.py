import logging

# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.ERROR)

def solve(s):
    cakes = list(s)
    cakes.reverse()
    count = 0
    check = '-'
    for ii, i in enumerate(cakes):
        if i is check:
            count += 1
            check = '+' if check is '-' else '-'
            logging.debug(repr(cakes[0:ii]) + ' next ' + check)

    return count


# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  s = raw_input()
  m = solve(s)
  print "Case #{}: {}".format(i, m)
  # check out .format's specification for more formatting options