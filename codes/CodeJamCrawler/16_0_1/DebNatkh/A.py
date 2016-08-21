def	mn(n, i):
	print("Case #", i, ": ", end = "", sep = "")
	if (n == 0):
		print("INSOMNIA")
	else:
		s = set()
		i = 1
		while (len(s) != 10):
			s |= set(list(map(str, str(i * n))))
			i += 1
		print((i - 1) * n)

m = int(input())
for i in range(m):
	t = int(input())
	mn(t, i+1)