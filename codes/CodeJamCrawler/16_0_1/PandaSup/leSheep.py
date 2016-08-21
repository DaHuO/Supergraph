tc = int(input())
for i in range(1, tc+1):
	n = int(input())
	if n == 0:
		print("Case #{}: {}".format(i, "INSOMNIA"))
	else:
		digitsSeen = set()
		digitsSeen.update(set(str(n)))
		c = 2
		while len(digitsSeen) != 10:
				N = c*n
				digitsSeen.update(set(str(N)))
				c += 1
		print("Case #{}: {}".format(i, N))


