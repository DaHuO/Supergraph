t = int(input())
for cs in range(t):
	st = input()
	s = [(0 if i == '+' else 1) for i in st]
	n = len(s)
	flips = 0
	for i in range(n-1, -1, -1):
		if (s[i] + flips) % 2 == 1:
			flips += 1
	print("Case #%d: %d" % (cs+1, flips))