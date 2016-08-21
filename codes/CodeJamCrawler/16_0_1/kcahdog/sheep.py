def inp():
	return int(raw_input().strip())

insomnia = 'INSOMNIA'

for qq in xrange(inp()):
	print 'Case #%d:' % (qq+1),
	n = inp()
	temp = n
	digits = {}
	for i in xrange(10):
		digits[i] = False
	
	if n == 0:
		print insomnia
		continue
	
	for pp in xrange(10**5):
		num = temp				
		while(num > 0):
			if not digits[num%10]:
				digits[num%10] = True
			num/=10		
		cnt = 0
		for i in xrange(10):
			if digits[i]:
				cnt+=1
		if cnt == 10:
			print temp
			break
		temp += n

	for i in xrange(10):
		if not digits[i]:
			print insomnia
			break