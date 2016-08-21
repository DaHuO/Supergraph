import sys

def answer(n):
	i = 1
	digits = range(0, 10)
	while i < 10 ** 7:
		num = i * n
		for digit in str(num):
			if int(digit) in digits:
				digits.remove(int(digit))
		if digits == []:
			return num
		i += 1
	return 'INSOMNIA'

if __name__ == '__main__':
	f = sys.stdin
	fn = sys.argv[1]
	f = open(fn)
	if len(sys.argv) == 3:
		output = open(sys.argv[2], 'w')
	t = int(f.readline())
	for _t in xrange(t):
		n = int(f.readline().strip())
		print n
		ans = answer(n)
		if len(sys.argv) == 3:
			output.write('Case #%d: %s' % (_t+1, ans) + '\n')
		print 'Case #%d: %s' % (_t+1, ans)
