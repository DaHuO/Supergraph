tests = int(input())
for case in range(1, tests + 1):
	N = int(input())
	if N == 0:
		print("Case #" + str(case) + ": INSOMNIA")
	else:
		n = N
		tab = [0] * 10
		count = 0
		while count < 10:
			s = str(n)
			for c in s:
				if tab[int(c) - int('0')] == False:
					count += 1
				tab[int(c) - int('0')] = True
			n += N
		print("Case #" + str(case) + ": " + str(n - N))
