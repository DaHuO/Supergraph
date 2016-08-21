# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n = int(raw_input())
  dic = set([0,1,2,3,4,5,6,7,8,9])
  if n == 0:
  	print "Case #{}: {}".format(i, "INSOMNIA")
  else:
  	index = 1;
  	while dic:
  		origin = n * index
  		tmp = origin
  		#print "Test " + str(origin)
  		while tmp != 0:
  			digit = tmp % 10
  			#print digit
  			if digit in dic:
  				dic.remove(digit)
  				if not dic:
  					print "Case #{}: {}".format(i, origin)
  					break
  			tmp = tmp / 10
  		index = index + 1
  		#print dic
  	

  # check out .format's specification for more formatting options