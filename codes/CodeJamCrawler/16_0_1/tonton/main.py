import logging

# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.ERROR)

def solve(n):
    if n is 0:
        return "INSOMNIA"

    numbers = set()
    for i in range(1, 1000000):
        n_i = i * n
        logging.debug("N*" + repr(i) + " = " + repr(n_i))
        n_i_str = sorted((str(n_i)))
        numbers = numbers.union(n_i_str)
        logging.debug(numbers)
        if len(numbers) is 10:
            return n_i

    logging.error("over " + repr(i) + " times!")


# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  l = [int(s) for s in raw_input().split(" ")]  # read a list of integers
  m = solve(l[0])
  print "Case #{}: {}".format(i, m)
  # check out .format's specification for more formatting options