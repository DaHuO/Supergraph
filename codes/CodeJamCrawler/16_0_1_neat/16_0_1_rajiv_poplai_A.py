# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
	m = 1
	for s in raw_input().split(" "):
		n = int(s)   # read a list of integers, 2 in this case
		if (n == 0):
			print "Case #{}: INSOMNIA".format(i )
			break
		result = n
		a = []
		for j in xrange(0,10):
			a.append(False)
		found = False
		while (found == False):	
			m = m + 1
			strResult = str(result)
			for ch in strResult:
				a[int(ch)] = True
			#print result, a	
			k = 0
			while k < 10:
				if a[k] is False:
					break
				k = k + 1
			if (k == 10):
				print "Case #{}: {}".format(i, result )
				found = True
			try:
				result =  n*m
			except:
				found = True
			
				
		#	while (found is not true):
		#	print "Case #{}: {} {}".format(i, outNum )
  			# check out .format's specification for more formatting options