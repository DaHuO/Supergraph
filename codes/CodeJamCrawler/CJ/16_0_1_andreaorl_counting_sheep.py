#!/usr/bin/python

f = open('A-large.in', 'r')
o = open('output', 'w')

T = f.readline()
digits = []
for x in xrange(0, 10):
	digits.append(False)

def all_true():
	out = True
	print digits
	for x in xrange(0, 10):
		print digits[x]
		if (digits[x] is False): 
			out = False 
			break
	return out


for x in range(1, int(T)+1):
	N = f.next()


	for a in xrange(0, 10):
		digits[a] = False
	stop = False
	count = 1
	result = "INSOMNIA"
	if (int(N) == 0):
		pass
	else:
		while (count < 100000):
			M = str(int(N) * count)

			for i in xrange(0, len(M)):
				digit = int(M[i])
				print digit
				digits[digit] = True
				if (all_true()): 
					result = M
					print "result: " + result
					stop = True
					break
			if (stop):
				break
			count += 1

	o.write("Case #" + str(x) + ": " + result + '\n')


