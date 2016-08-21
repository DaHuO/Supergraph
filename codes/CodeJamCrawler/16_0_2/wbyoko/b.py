N = int(raw_input())

for T in range(N):
	stack = list(raw_input())
	polarity = 0
	current = ""
	for pole in stack:
		if current != pole:
			polarity += 1
			current = pole

	print "Case #%d: %s" % (T+1, (polarity - 1) + (0 if current == "+" else 1))
