import logging
# logging.basicConfig(level=logging.DEBUG)

def add(n1, n2):
	SUM = []
	carry = 0
	for d1,d2 in map(None,n1,n2):
		if d1 is None:
			d1 = 0
		if d2 is None:
			d2 = 0
		s = carry + d1 + d2
		if s > 9:
			d = s % 10
			carry = s / 10
		else:
			d = s
			carry = 0
		SUM.append(d)
	if carry != 0:
		SUM.append(carry)
	logging.debug('sum:' + str(SUM))
	return SUM

def toint(sum):
	s = 0
	for i, d in enumerate(sum):
		s += d * (10 ** (i))
	return s

def solving(line):
	N = []
	sleep = [0] * 10
	for d in line:
		if d.isdigit():
			N.insert(0,int(d))
	if N[-1] == 0:
		return 'INSOMNIA'
	logging.debug('input:' + str(N))
	SUM = [0]
	while True:
		SUM = add(SUM, N)
		for d in SUM:
			sleep[d] = 1
		if sum(sleep) == 10:
			break
	return str(toint(SUM))


with open('input', 'r') as input:
	count = 0
	for line in input:
		if count == 0:
			count+=1
			continue
		print 'Case #%d: %s' % (count, solving(line))
		count+=1