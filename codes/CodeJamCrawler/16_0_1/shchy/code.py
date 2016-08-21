# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n= int(raw_input())
  array = [0]*10
  found = 0
  if n == 0:
  	print "Case #{}: {}".format(i, "INSOMNIA")
  	continue
  origin = n
  while found!=10:
  	n_string = str(n)
  	for ch in n_string:
  		if array[int(ch)] == 0:
  			array[int(ch)] = 1
  			found = found + 1
  	n = n+origin
  print "Case #{}: {}".format(i, n-origin)
  # check out .format's specification for more formatting options