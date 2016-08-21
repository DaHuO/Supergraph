n = []
t = input()
for _ in xrange(t):
	#print t	
	n.append(input())
c = 1
all_numbers = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
for i in n:
	if i == 0:
		print "Case #" + str(c) + ": INSOMNIA"
	else: 
		nums = set(list(str(i)))
		if nums == all_numbers:
			print "Case #" + str(c) + ": " + str(i)
		else:
			m = 2
			while nums != all_numbers:
				t = i * m
				nums |= set(list(str(t)))
				m += 1
			print "Case #" + str(c) + ": " + str(t)
	c += 1
