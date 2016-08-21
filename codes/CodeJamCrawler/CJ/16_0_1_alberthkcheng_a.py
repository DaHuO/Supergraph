n = int(raw_input())



def get_last_number(N):
	s = "Wrong number"
	if N == 0:
		s = "INSOMNIA"
	else:
		old = N
		l = set(map(str,range(10)))
		while len(l) > 0:
			ns = set(list(str(N)))
			# print 'length of l: ' + str(len(l))
			# print N
			l = l - ns
			lastN = N
			N += old
		s = str(lastN)
	return s



for i in range(n):
	N = int(raw_input())
	print "Case #" + str(i+1) + ": " + get_last_number(N)