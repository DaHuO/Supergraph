out = open('outputA_l.txt', 'w')
with open('A-large.in', 'r') as f:
	T = int(f.readline())
	for i in range(1, T+1):
		out.write('Case #%s: ' % i)
		N = int(f.readline())
		if N == 0:
			# print "INSOMNIA"
			out.write('INSOMNIA\n')
		else:
			digits = dict()
			count = 0
			n = 0
			while len(digits) < 10:
				n += N
				curr = n
				while curr != 0:
					d = curr % 10
					if d not in digits:
						digits[d] = 1
					curr = curr / 10
				count += 1
			# print n
			out.write('%s\n' % n)

out.close()

