c = input()
case = 1
while case <= c:
	#print case, c
	n = input()
	
	if n == 0:
		print "Case #"+str(case)+": INSOMNIA"
		case += 1
		continue

	hasSeen = 10 * [False]
	
	m = 0
	while reduce(lambda x, y: x and y, hasSeen, True) != True:
		m += 1
		tmp = m * n
		
		while tmp:
			hasSeen[tmp%10] = True
			#print hasSeen
			tmp /= 10

	
	print "Case #" + str(case) + ": " + str(m*n)
		
	case += 1