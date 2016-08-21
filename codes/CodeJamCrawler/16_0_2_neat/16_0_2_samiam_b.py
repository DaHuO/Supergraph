def solve(x):
	#print x
	length = len(x)
	#print("length: "+str(length))
	count = 0
	
	if "-" in x[length-1]:
		#print "bump"
		count += 1
	
	for i in range(length-1):
		#print(str(i))
		#print x[i] + " then " + x[i+1]

		if not x[i] in x[i+1]:
			#print "bump" + str(i)
			count += 1
	#print count
	return str(count)
	
	

T = int(raw_input())
for t in range(T):
	n = raw_input()
	
	print 'Case #' + str(t+1) + ": " + solve(n)
