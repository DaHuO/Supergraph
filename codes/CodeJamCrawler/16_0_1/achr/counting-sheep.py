T = int(input())

for testIndex in range(1, T+1):
	N = int(input())

	if N == 0:
		print("Case #{0}: INSOMNIA".format(testIndex))
	else:
		digits = set()
		baseN = N
		while len(digits) < 10:
			digits.update(str(N))

			if len(digits) < 10:
				N += baseN

		print("Case #{0}: {1}".format(testIndex, N))