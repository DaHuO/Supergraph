#!/usr/bin/env python3

cases = int(input())

for i in range(cases):
	n = int(input())
	m = 0
	if n == 0:
		print("Case #{}: INSOMNIA".format(i + 1))
		continue
	seen = set()
	while len(seen) < 10:
		m += n
		ns = str(m)
		for d in ns:
			seen.add(d)
	print("Case #{}: {}".format(i + 1, m))
