import sys
T = case = -1
file = open(sys.argv[1], 'r')

for x in file:
	x = x.strip()
	case += 1
	if case==0:
		T = int(x)
		continue
	res = x[0]
	for i in range(1, len(x)):
		if ord(x[i]) >= ord(res[0]):
			res = x[i] + res
		else:
			res = res + x[i]
	print 'Case #%d:' % case, res
	if case==T:
		break
