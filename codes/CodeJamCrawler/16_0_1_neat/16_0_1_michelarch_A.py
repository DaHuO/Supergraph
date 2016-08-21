
T = int(input())

for t in range(T):
	d = set()
	N = int(input())
	if N == 0:
		print("Case #" + str(t+1) + ": INSOMNIA")
		continue
	i = 1
	while len(d) < 10:
		for c in str(i*N):
			d.add(c)
		
		i += 1
	print("Case #" + str(t+1) + ": " + str((i-1) * N))


