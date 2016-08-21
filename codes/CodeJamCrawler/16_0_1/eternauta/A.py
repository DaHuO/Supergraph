INF = 1000


def getDigits(n):
	return set(map(int, list(str(n))))

T = input()

for t in range(1, T+1):
	N = input()

	if N == 0:
		res = "INSOMNIA"
	else:
		digits = set()
		for i in range(1, INF):
			digits.update(getDigits(N*i))
			if len(digits) == 10:
				res = N*i
				break

	print "Case #%d: %s" % (t, res)

