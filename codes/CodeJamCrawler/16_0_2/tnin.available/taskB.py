import sys
T = case = -1
file = open(sys.argv[1], 'r')

for x in file:
	case += 1
	if case==0:
		T = int(x)
		continue
	
	print 'Case #%d:' % case,
	pcakes = 0
	x = x.strip()
	for i in range(len(x)):
		if x[i]=='-': pcakes += 2**i

	for flips in range(777):
		if pcakes==0: break
		L = len(bin(pcakes))-2
		pcakes ^= (1<<L) - 1
		
	print flips
	if case==T:
		break
