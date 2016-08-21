for i in range(int(input())):
	flips, n = 0, [0 if c == '-' else 1 for c in input()]
	for j in range(len(n)-1, -1, -1):
		if n[j]: n.pop()
		else: break
	if len(n) in (0, 1):
		flips = len(n)
	else:
		for j in range(1, len(n)):
			if n[j-1] != n[j]:
				flips += 1
		flips += 1
	print("Case #{}: {}".format(i+1, flips))