import sys

t = int(raw_input())
case = 0
while t>0:
	t-=1
	case += 1
	print "Case #"+str(case)+":",

	result = [0 for a in range(10)]
	n = int(input())
	N = n
	if n==0:
		print 'INSOMNIA'
		continue
	count = 0
	while count<10:
		s = str(n)
		for a in s:
			if result[int(a)] == 0:
				count += 1
				result[int(a)] += 1
		if count<10:
			n += N
	print n
