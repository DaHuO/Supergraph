import sys
T = case = -1
file = open(sys.argv[1], 'r')

for x in file:
	case += 1
	N = int(x)
	if case==0:
		T = N
		continue
	if N==0:
		print 'Case #%d: INSOMNIA' % case
		if case==T:	break
		else:		continue
	count = mask = 0
	for i in xrange(1, 10000):
		n = N * i
		while n:
			lastDigit = n%10
			if (mask & (1<<lastDigit)) == 0:
				count += 1
				mask |= (1<<lastDigit)
			n = (n - lastDigit) / 10
		if count==10:
			print 'Case #%d:' % case, N*i
			break
	if case==T:
		break
