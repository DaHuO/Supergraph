t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  K, C, S = [int(x) for x in raw_input().split(" ")]  # read a list of integers, 3 in this case
  o = ' '.join(str(x) for x in range(1, K+1))
  print "Case #{}: {}".format(i, o)
