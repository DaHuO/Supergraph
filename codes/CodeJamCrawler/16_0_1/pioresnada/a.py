def f():
	n = int(input())
	if not n: return "INSOMNIA"
	s, m = 0, 0
	while s != 0x3ff:
		m = m + n
		for c in str(m):
			s = s | (1 << int(c))
	return m

for i in range(int(input())): print("Case #{0}: {1}".format(i+1, f()))

