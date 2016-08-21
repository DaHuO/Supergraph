T = input()
# T = 2001
for i in range(T):
	n = input()
	# n = i
	if n == 0:
		print 'Case #'+ str(i+1) +': INSOMNIA'
	else:
		s = set()
		count = 1
		while len(s) != 10:
			x = count*n
			# print x
			d = str(x)
			d = list(d)
			for j in d:
				s.add(j)
			# print s
			count += 1
		print 'Case #' + str(i+1) + ': '+ str(x)

