#!/usr/bin/env sage

for t in [1 .. input()]:
	N, J = map(int, raw_input().split())
	now = (1 << N -1) | 1
	while now % 3: now += 2
	print "Case #%d:"% t
	while J:
		s = bin(now)[2:]
		ok = True
		for b in [3 .. 10]:
			t = int(s, b)
			if is_prime(t):
				ok = False
				break
		if ok:
			d = [divisors(int(s, b))[1] for b in [2..10]]
			J -= 1
			print s, ' '.join(map(str, d))
		now += 6

