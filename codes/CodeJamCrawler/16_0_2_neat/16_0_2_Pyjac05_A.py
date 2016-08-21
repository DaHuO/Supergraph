l = input()
for z in range(0, l):
	N = input()
	seen = set()
	i = 1
	nu = set(range(0,10))
	if N == 0:
		print "Case #{0}: INSOMNIA".format(z + 1)
		continue
	while True:
		v = i * N;
		seen = seen | set(map(int, set(str(v))))
		if len(nu.difference(seen)) == 0:
			print "Case #{0}: {1}".format(z + 1, v)
			break
		i= i + 1