import sys
T = case = -1
file = open(sys.argv[1], 'r')

for x in file:
	case += 1
	x = x.split(' ')
	K = int(x[0])
	if case==0:
		T = K
		continue
	
	print 'Case #%d:' % case,
	for i in range(1, K+1): print i,
	print

	if case==T:
		break
