def solve():
	n = int(raw_input())
	out = "INSOMNIA"
	if n != 0:
		k = [False for i in range(10)]
		start = 1
		count = 10
		while count > 0:
			out = start * n
			digits = [ord(p) - ord('0') for p in str(out)]
			for d in digits:
				if not k[d]:
					count -= 1
					k[d] = True
			start += 1
	return out
t = int(raw_input())
for i in range(t):
	print 'Case #%d: %s' % (i + 1, solve())
