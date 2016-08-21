def flip(s, n):
	l = []
	for i in xrange(1, n+1):
		#print n, i, s[n-i]
		if (s[n-i] == '-'):
			l.append('+')
		else:
			l.append('-')
	return ''.join(l)

#s = '+-' 
#o = s
#print s, flip(s,1)+o[]

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
#t = 0
for i in xrange(1, t + 1):
  s = raw_input().strip()# read a list of integers, 2 in this case
  n = len(s)
  j = 0
  o = s
  numFlips = 0
  while (j < n):
  	#print j, n, s, numFlips
  	if ((j+1) == n): 
  		if (s[j] == '-'):
  			s = flip(s, j+1)
  			numFlips = numFlips + 1
  	else:
  	    if (not (s[j] == s[j+1])):
	  		s = flip(s, j+1) + o[(j+1):]
	  		numFlips = numFlips + 1
	  		#j = j + 1
	j = j + 1
  print "Case #{}: {}".format(i, numFlips)
  # check out .format's specification for more formatting options