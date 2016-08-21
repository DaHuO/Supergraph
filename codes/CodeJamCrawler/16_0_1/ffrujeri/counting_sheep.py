T = int(raw_input())
t = 1
while t <= T:
	seen_digits = set()
	N = int(raw_input())

	if N == 0:
		print("Case #%d: INSOMNIA" % t)
		t += 1
		continue

	cur = N
	while(len(seen_digits) < 10):
		for d in str(cur):
			seen_digits.add(d)
		cur += N
	
	cur -= N

	print("Case #%d: %d" % (t, cur))
	t += 1
