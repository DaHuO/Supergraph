#Counting Sheep
num = int(raw_input())

for i in range(1, num+1):
	s = raw_input()
	# print s
	if int(s) == 0:
		print "Case #{0}: INSOMNIA".format(i)
		continue

	m = 1
	digits = []
	while True:
		for c in str(m*int(s)):
			if int(c) not in digits:
				digits.append(int(c))
		
		if len(digits) == 10 or m > 100000:
			break
		# print digits
		m+=1

	if len(digits) == 10:
		print "Case #{0}: {1}".format(i, m* int(s))
	else:
		print "Case #{0}: INSOMNIA".format(i)