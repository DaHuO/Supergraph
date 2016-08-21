# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n= str(raw_input())
  opt = 0;
  if n[-1] == "-":
  	opt = 1
  for j in xrange(len(n)-1, 0, -1):
  	idx=j-1
  	if n[idx]!=n[idx+1]:
  		opt = opt + 1
  print "Case #{}: {}".format(i, opt)
  # check out .format's specification for more formatting options