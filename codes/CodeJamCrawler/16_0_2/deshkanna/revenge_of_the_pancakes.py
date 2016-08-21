import itertools

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  l = list(raw_input())  # convert string to characters
  o = len(list(itertools.groupby(list(l), lambda x: x == '-'))) - 1 + int(list(l)[-1]=='-')
  print "Case #{}: {}".format(i, o)
