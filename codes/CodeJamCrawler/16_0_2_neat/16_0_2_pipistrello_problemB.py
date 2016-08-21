
T = int(raw_input())
for i in xrange(T):
	N = raw_input()
	N = N.replace('+','1')
	N = N.replace('-','0')
	print 'Case #'+ str(i+1) + ':',

	newstring = N[0]
	for char in N[1:]:
		if char != newstring[-1]:
			newstring += char 		

	N = newstring

	if (N[0] == '0' and len(N)%2 == 0) or (N[0] == '1' and len(N)%2 == 1):
		print len(N)-1
	else:
		print len(N)
