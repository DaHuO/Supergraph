#! /usr/bin/python2
cases = []
fil = open('A-large.in','r')
T = int(fil.readline().split('\n')[0])
for i in range(1,T+1):
	cases.append(int(fil.readline().split('\n')[0]))
digits = (0,1,2,3,4,5,6,7,8,9)
acqdigits = []
for index,value in enumerate(cases):
	temp = value
	count = 1
	while 1:
		if not value:
			print 'case #%d: INSOMNIA' %(index+1)
			break
		else:
			digit = temp % 10
			temp /= 10
			acqdigits.append(digit)
			if set(acqdigits) == set(digits):
				print 'Case #%d: %d' %((index+1),(value*count))
				acqdigits = []
				break
			elif not temp:
				count += 1
				temp = value
				temp *= count 
