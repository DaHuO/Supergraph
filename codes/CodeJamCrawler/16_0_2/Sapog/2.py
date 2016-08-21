T = int(input())
for t in range(T):
	s = [c == '+' for c in input()]
	res = 0
	sign = True
	for sgn in reversed(s):
		if sgn != sign:
			res += 1
			sign = not sign
	print('Case #{}: {}'.format(t + 1, res))
